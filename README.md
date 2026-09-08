# MicroLLM Text Adventure

- **Micro-LLM Text-Based Adventure Game:** A low-latency interactive fiction engine driven by a fine-tuned 1B–3B parameter LLM for dynamic story narration, choice parsing, and game state updates.
- **Text-Driven & LLM-Generated Gameplay:** Model outputs structured responses (narration, story choices, state deltas) guided by modular genre system prompts and deterministic RAG (vector database) lookups for fixed lore anchors and world canon.
- **Visual Integration:** Reactive UI/rendering pipeline that maps LLM-generated visual keys to pre-rendered asset banks, procedural shaders (scanlines, film grain, vignette), and genre-specific visual themes.
- **Infrastructure & Deployment:** Full-stack architecture featuring containerized backend orchestrators (FastAPI/Go), optimized inference runners (vLLM / llama.cpp GGUF), embedded vector storage (ChromaDB/LanceDB), Terraform IaC, and automated CI/CD workflows.
- **Fine-Tuned Model:** Base model optimized for low token count footprints, strict JSON/structured delimiter outputs, and genre-specific tone adaptability using on-the-fly LoRA adapters.

## Current (mock)

Playable core: pick a genre, play a short beat-graph story, and get the same JSON a later model must emit (`narration`, `choices`, `state_delta`, `visual_key`, `game_over`, `ending`). The narrator is a deterministic mock so the UI and game loop work without a live LLM.

## Next (real model)

Swap `MockNarrator` for an inference runner that returns the same `TurnResponse` schema. RAG, LoRA adapters, and GGUF serving stay out of this pass.

## Run

From the repo root (on Windows, `py -3` if `python` is not on PATH):

```bash
py -3 -m pip install -r backend/requirements.txt
py -3 -m uvicorn backend.app:app --reload --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000 — choose a genre, click choices or type free text, then start a new game when the file closes.
