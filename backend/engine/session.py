from __future__ import annotations

from dataclasses import dataclass, field

from .schema import GameStatePublic, StateDelta

MAX_HISTORY = 8
STAT_CAPS = {"hp": 10, "tension": 10}


@dataclass
class GameSession:
    session_id: str
    genre: str
    location: str = "unknown"
    inventory: list[str] = field(default_factory=list)
    flags: dict[str, str | bool | int] = field(default_factory=dict)
    stats: dict[str, int] = field(default_factory=lambda: {"hp": 10, "tension": 2})
    beat: str = "opening"
    turn_index: int = 0
    game_over: bool = False
    last_choices: list[dict[str, str]] = field(default_factory=list)
    history: list[dict] = field(default_factory=list)

    def apply_delta(self, delta: StateDelta) -> None:
        if delta.location:
            self.location = delta.location
        for item in delta.inventory_add:
            if item not in self.inventory:
                self.inventory.append(item)
        for item in delta.inventory_remove:
            if item in self.inventory:
                self.inventory.remove(item)
        self.flags.update(delta.flags)
        for key, change in delta.stats.items():
            current = self.stats.get(key, 0) + change
            cap = STAT_CAPS.get(key)
            if cap is not None:
                current = max(0, min(cap, current))
            else:
                current = max(0, current)
            self.stats[key] = current

    def remember(self, player_input: str | None, turn_payload: dict) -> None:
        if player_input is not None:
            self.history.append({"role": "player", "text": player_input})
        self.history.append({"role": "narrator", "turn": turn_payload})
        self.history = self.history[-(MAX_HISTORY * 2) :]

    def public(self) -> GameStatePublic:
        return GameStatePublic(
            location=self.location,
            inventory=list(self.inventory),
            flags=dict(self.flags),
            stats=dict(self.stats),
            genre=self.genre,
            turn_index=self.turn_index,
            game_over=self.game_over,
        )
