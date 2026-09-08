from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.engine.flavor import FLAVORS
from backend.engine.genres import get_genre, list_genres
from backend.engine.mock_narrator import MockNarrator
from backend.engine.schema import NewGameRequest, TurnEnvelope, TurnRequest
from backend.engine.session import GameSession

ROOT = Path(__file__).resolve().parent.parent
GAME_DIR = ROOT / "game"

app = FastAPI(title="MicroLLM Text Adventure", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

_sessions: dict[str, GameSession] = {}
_narrator = MockNarrator()


@app.get("/api/genres")
def api_genres():
    return list_genres()


@app.post("/api/new", response_model=TurnEnvelope)
def api_new(req: NewGameRequest):
    genre = req.genre.strip()
    try:
        get_genre(genre)
    except KeyError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    if genre not in FLAVORS:
        raise HTTPException(status_code=400, detail=f"No mock flavor pack for '{genre}'")
    session_id = uuid4().hex[:12]
    session = GameSession(session_id=session_id, genre=genre)
    turn = _narrator.opening(session)
    session.remember(None, turn.model_dump())
    _sessions[session_id] = session
    return TurnEnvelope(session_id=session_id, turn=turn, state=session.public())


@app.post("/api/turn", response_model=TurnEnvelope)
def api_turn(req: TurnRequest):
    session = _sessions.get(req.session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Unknown session")
    if session.game_over:
        raise HTTPException(status_code=409, detail="Story already closed. Start a new game.")
    if not req.input.strip():
        raise HTTPException(status_code=400, detail="Empty input")
    turn = _narrator.step(session, req.input)
    session.remember(req.input, turn.model_dump())
    return TurnEnvelope(session_id=session.session_id, turn=turn, state=session.public())


app.mount("/", StaticFiles(directory=str(GAME_DIR), html=True), name="game")
