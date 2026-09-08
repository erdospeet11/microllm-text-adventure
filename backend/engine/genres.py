from __future__ import annotations

import json
from pathlib import Path

from .schema import GenreInfo

ROOT = Path(__file__).resolve().parent.parent.parent
GENRES_DIR = ROOT / "prompts" / "genres"

TITLES = {
    "scifi": "Science Fiction",
    "horror": "Horror",
    "noir_crime": "Noir Crime",
    "romcom": "Romantic Comedy",
    "wuxian": "Wuxia",
    "war_story": "War Story",
    "urban_fantasy": "Urban Fantasy",
    "apocalypse": "Apocalypse",
    "postapocaliptic": "Post-Apocalyptic",
    "cold_war_spy_setting": "Cold War Spy",
}

_cache: dict[str, dict] | None = None

def _load_all() -> dict[str, dict]:
    global _cache
    if _cache is None:
        loaded: dict[str, dict] = {}
        for path in sorted(GENRES_DIR.glob("*.json")):
            loaded[path.stem] = json.loads(path.read_text(encoding="utf-8"))
        _cache = loaded
    return _cache

def list_genres() -> list[GenreInfo]:
    out: list[GenreInfo] = []
    for genre_id, data in _load_all().items():
        features = data.get("core_features") or []
        out.append(
            GenreInfo(
                id=genre_id,
                title=TITLES.get(genre_id, genre_id.replace("_", " ").title()),
                blurb=features[0] if features else data.get("tone_guidelines", ""),
                tone=data.get("tone_guidelines", ""),
            )
        )
    return out

def get_genre(genre_id: str) -> dict:
    genres = _load_all()
    if genre_id not in genres:
        known = ", ".join(sorted(genres))
        raise KeyError(f"Unknown genre '{genre_id}'. Known: {known}")
    return genres[genre_id]

def title_for(genre_id: str) -> str:
    return TITLES.get(genre_id, genre_id.replace("_", " ").title())
