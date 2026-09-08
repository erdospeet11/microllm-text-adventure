from __future__ import annotations

import re

from .flavor import BEAT_ORDER, FLAVORS, LOCATION_BY_BEAT, VISUAL_BY_BEAT
from .genres import get_genre, title_for
from .schema import Choice, StateDelta, TurnResponse
from .session import GameSession

_STOP = {
    "a",
    "an",
    "the",
    "to",
    "of",
    "and",
    "or",
    "for",
    "with",
    "your",
    "you",
    "in",
    "on",
    "at",
    "into",
    "from",
}

def _tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in _STOP and len(w) > 1}

def match_choice(raw: str, choices: list[Choice]) -> str:
    text = raw.strip().lower()
    if not choices:
        return "a"
    if text in {"1", "2", "3"}:
        idx = int(text) - 1
        if 0 <= idx < len(choices):
            return choices[idx].id
    for choice in choices:
        if text == choice.id.lower() or text == choice.label.lower():
            return choice.id
    best_id = choices[0].id
    best_score = 0
    incoming = _tokens(text)
    for choice in choices:
        score = len(incoming & _tokens(choice.label))
        if choice.id.lower() in incoming:
            score += 3
        if score > best_score:
            best_score = score
            best_id = choice.id
    return best_id

def _choices_for(beat: str, flavor: dict, inventory: list[str]) -> list[Choice]:
    item = flavor["item"]
    threat = flavor["threat"]
    ally = flavor["ally"]
    if beat == "opening":
        labels = [
            ("a", f"Move carefully through {flavor['place']}"),
            ("b", f"Push straight toward {threat}"),
            ("c", f"Search the area for something like {item}"),
        ]
    elif beat == "probe":
        labels = [
            ("a", f"Follow the trail toward {ally}"),
            ("b", f"Ask {ally} the question nobody wants asked"),
            ("c", f"Hunt for proof of {threat}"),
        ]
    elif beat == "complication":
        use = (
            f"Spend {item} before it is too late"
            if item in inventory
            else f"Try to bluff without {item}"
        )
        labels = [
            ("a", "Take the risk while the window is open"),
            ("b", "Play it safe and keep your head down"),
            ("c", use),
        ]
    elif beat == "crisis":
        labels = [
            ("a", f"Confront {threat} directly"),
            ("b", f"Bargain with {ally} for a way through"),
            ("c", "Get out and live with what that costs"),
        ]
    elif beat == "climax":
        labels = [
            ("a", "Save the others first"),
            ("b", "Save yourself and the leverage you hold"),
            ("c", "Try to hold both, knowing something will tear"),
        ]
    else:
        labels = []
    return [Choice(id=cid, label=label) for cid, label in labels]

def _choice_effects(beat: str, choice_id: str, flavor: dict, inventory: list[str]) -> StateDelta:
    item = flavor["item"]
    delta = StateDelta()
    if beat == "opening":
        if choice_id == "a":
            delta.flags = {"approach": "cautious"}
            delta.stats = {"tension": 1}
        elif choice_id == "b":
            delta.flags = {"approach": "bold"}
            delta.stats = {"hp": -1, "tension": 2}
        else:
            delta.flags = {"approach": "observant"}
            delta.inventory_add = [item]
            delta.stats = {"tension": 1}
    elif beat == "probe":
        if choice_id == "a":
            delta.flags = {"lead": "followed"}
            delta.stats = {"tension": 1}
        elif choice_id == "b":
            delta.flags = {"talked": True}
            delta.stats = {"tension": 1}
        else:
            delta.flags = {"evidence": True}
            if item not in inventory:
                delta.inventory_add = [item]
            delta.stats = {"tension": 2}
    elif beat == "complication":
        if choice_id == "a":
            delta.flags = {"risk": True}
            delta.stats = {"hp": -2, "tension": 2}
        elif choice_id == "b":
            delta.flags = {"safe": True}
            delta.stats = {"tension": 1}
        elif item in inventory:
            delta.flags = {"used_item": True}
            delta.inventory_remove = [item]
            delta.stats = {"tension": -1}
        else:
            delta.flags = {"used_item": False}
            delta.stats = {"tension": 2}
    elif beat == "crisis":
        if choice_id == "a":
            delta.flags = {"method": "confront"}
            delta.stats = {"hp": -1, "tension": 2}
        elif choice_id == "b":
            delta.flags = {"method": "bargain"}
            delta.stats = {"tension": 1}
        else:
            delta.flags = {"method": "flee"}
            delta.stats = {"tension": 2}
    elif beat == "climax":
        if choice_id == "a":
            delta.flags = {"finale": "others"}
            delta.stats = {"hp": -1}
        elif choice_id == "b":
            delta.flags = {"finale": "self"}
            delta.stats = {"tension": 1}
        else:
            delta.flags = {"finale": "both"}
            delta.stats = {"hp": -2, "tension": 2}
    return delta

def pick_ending(flags: dict, stats: dict) -> str:
    hp = stats.get("hp", 10)
    tension = stats.get("tension", 0)
    finale = flags.get("finale")
    if hp <= 4 or (hp <= 6 and tension >= 8):
        return "grim"
    if flags.get("evidence") and flags.get("talked") and finale != "self":
        return "truth"
    if finale == "others" and flags.get("used_item"):
        return "hopeful"
    if flags.get("method") == "confront" and flags.get("approach") == "bold":
        return "pyrrhic"
    if finale == "self" or (
        flags.get("method") == "flee" and flags.get("approach") == "cautious"
    ):
        return "ambiguous"
    if flags.get("used_item") or flags.get("method") == "bargain":
        return "hopeful"
    return "bittersweet"


def _paragraphs(*parts: str) -> str:
    return "\n\n".join(p.strip() for p in parts if p and p.strip())


def _approach_line(flags: dict, flavor: dict) -> str:
    approach = flags.get("approach")
    if approach == "cautious":
        return f"You kept to the edges of {flavor['place']}, counting exits."
    if approach == "bold":
        return f"You went at {flavor['threat']} like time was already spent."
    if approach == "observant":
        return f"You catalogued the room until {flavor['item']} stopped being furniture."
    return ""

def narrate_beat(beat: str, session: GameSession, flavor: dict, genre: dict) -> str:
    required = (genre.get("must_include") or {}).get("required_elements") or []
    constraint = required[0] if required else flavor["hook"]
    if beat == "opening":
        return _paragraphs(
            f"{flavor['place'].rstrip('.')}. You are {flavor['you']}.",
            flavor["inciting"],
            f"At the center of it sits {flavor['hook']}. {constraint}",
        )
    if beat == "probe":
        extra = _approach_line(session.flags, flavor)
        return _paragraphs(
            extra,
            flavor["probe"],
            f"{flavor['ally']} is already part of the geometry. So is {flavor['threat']}.",
        )
    if beat == "complication":
        item_line = (
            f"The {flavor['item']} feels heavier now."
            if flavor["item"] in session.inventory
            else "Your pockets are honest: empty of leverage."
        )
        return _paragraphs(flavor["complication"], item_line)
    if beat == "crisis":
        return _paragraphs(
            flavor["crisis"],
            f"Tension sits at {session.stats.get('tension', 0)} and the body keeps its own score.",
        )
    if beat == "climax":
        return _paragraphs(
            flavor["climax"],
            f"This is the hour {title_for(session.genre)} stories do not let you postpone.",
        )
    ending_key = pick_ending(session.flags, session.stats)
    return _paragraphs(
        flavor["endings"][ending_key],
        "The engine marks the file closed. Nothing here was a joke, and nothing reset the world for free.",
    )

class MockNarrator:
    """Deterministic stand-in that emits the same TurnResponse a later LLM must produce."""

    def opening(self, session: GameSession) -> TurnResponse:
        return self._render(session, player_delta=StateDelta())

    def step(self, session: GameSession, raw_input: str) -> TurnResponse:
        current = session.beat
        choices = [Choice(**c) for c in session.last_choices]
        choice_id = match_choice(raw_input, choices)
        flavor = FLAVORS[session.genre]
        player_delta = _choice_effects(current, choice_id, flavor, session.inventory)
        player_delta.flags = {**player_delta.flags, "last_choice": choice_id}
        idx = BEAT_ORDER.index(current)
        session.beat = BEAT_ORDER[min(idx + 1, len(BEAT_ORDER) - 1)]
        return self._render(session, player_delta)

    def _render(self, session: GameSession, player_delta: StateDelta) -> TurnResponse:
        flavor = FLAVORS[session.genre]
        genre = get_genre(session.genre)
        beat = session.beat
        loc_key = LOCATION_BY_BEAT[beat]
        location = flavor[loc_key]
        merged = StateDelta(
            location=location,
            inventory_add=list(player_delta.inventory_add),
            inventory_remove=list(player_delta.inventory_remove),
            flags=dict(player_delta.flags),
            stats=dict(player_delta.stats),
        )
        session.apply_delta(merged)
        game_over = beat == "ending"
        ending = pick_ending(session.flags, session.stats) if game_over else None
        if game_over:
            session.game_over = True
        choices = [] if game_over else _choices_for(beat, flavor, session.inventory)
        session.last_choices = [c.model_dump() for c in choices]
        session.turn_index += 1
        return TurnResponse(
            narration=narrate_beat(beat, session, flavor, genre),
            choices=choices,
            state_delta=merged,
            visual_key=VISUAL_BY_BEAT[beat],
            game_over=game_over,
            ending=ending,
        )
