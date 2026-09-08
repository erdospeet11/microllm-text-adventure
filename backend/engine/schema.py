from pydantic import BaseModel, Field

class Choice(BaseModel):
    id: str
    label: str

class StateDelta(BaseModel):
    location: str | None = None
    inventory_add: list[str] = Field(default_factory=list)
    inventory_remove: list[str] = Field(default_factory=list)
    flags: dict[str, str | bool | int] = Field(default_factory=dict)
    stats: dict[str, int] = Field(default_factory=dict)

class TurnResponse(BaseModel):
    narration: str
    choices: list[Choice] = Field(default_factory=list)
    state_delta: StateDelta = Field(default_factory=StateDelta)
    visual_key: str = "threshold"
    game_over: bool = False
    ending: str | None = None

class NewGameRequest(BaseModel):
    genre: str

class TurnRequest(BaseModel):
    session_id: str
    input: str

class GameStatePublic(BaseModel):
    location: str
    inventory: list[str]
    flags: dict[str, str | bool | int]
    stats: dict[str, int]
    genre: str
    turn_index: int
    game_over: bool

class TurnEnvelope(BaseModel):
    session_id: str
    turn: TurnResponse
    state: GameStatePublic

class GenreInfo(BaseModel):
    id: str
    title: str
    blurb: str
    tone: str