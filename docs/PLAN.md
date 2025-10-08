# Skippy Development Plan

## 1. Orientation
- Review `README.md` and proposed package layout (`src/skippy/**`) so directory purposes are clear.
- Trace existing flow: start at `run/discord/discord.py`, follow calls into `handler.py` and `gpt.py`, note missing imports or secrets.
- Sketch an updated architecture diagram (paper or whiteboard) showing Discord events → handlers → services → storage.

## 2. Environment & Tooling
- Set up a Python 3.11 virtual environment; install base deps (`discord.py`, `openai`, `pydantic`, `langchain`, `chromadb` or `faiss`, `python-dotenv`).
- Create `.env.example`; move real secrets to `.env` (gitignored) and load them via a typed `Config` class.
- Add `pyproject.toml` or `requirements.txt` with pinned versions; configure `ruff` + `black` or `ruff format` for consistency.

## 3. Core Design (Discord Bot)
- Build `src/skippy/discord_bot.py` that wires intents, command prefix, and dependency injection (config, services).
- Move message handling logic into `src/skippy/handlers/message_handler.py`; keep async functions slim and offload external calls to services.
- Define a context store abstraction (`ContextStore` interface) with a file-backed prototype, so swapping to Redis/DB later is easy.

## 4. Services & Integrations
- OpenAI: create `OpenAIChatService` (async) that formats prompts, handles retries/limits, and logs usage.
- YouTube: wrap the Data API search in `YouTubeService`; isolate all Google client code here.
- Token safety: replace `api/token_manager.py` and `api/crypt.py` with the new config module; delete plaintext/binary token artifacts once migrations are done.

## 5. RAG & Agentic Additions
- Collect conversation snippets or knowledge-base documents into a `data/knowledge/` folder (markdown or JSON).
- Use LangChain to:
  - Build an embeddings index (e.g., `OpenAIEmbeddings` + `Chroma`).
  - Create a retrieval chain that augments the system/user message before sending to OpenAI.
- For “agentic” behavior, experiment with LangChain tools (YouTube search, web summaries) but guard behind explicit commands or rate limits.
- Persist conversation turn history in the context store so RAG can ground replies on channel history.

## 6. Quality & Testing
- Add unit tests (pytest) for context store, message routing, and RAG pipeline (mock external APIs).
- Write integration smoke tests that simulate a Discord message event and verify the handler requests services correctly (using dependency injection + fakes).
- Enable structured logging and basic telemetry (log levels, timing).

## 7. Documentation & Learning Checkpoints
- Document setup, running, and testing steps in `README.md`.
- Keep notes on design decisions: why certain libraries, how secrets flow, how RAG is structured.
- After each major section, challenge yourself to explain the component aloud or in notes; refactor anything you cannot describe clearly.

## 8. Launch Checklist
- Secrets rotated and stored securely.
- Bot runs via `python -m skippy.cli discord`.
- Observability enabled (logs, error alerts).
- RAG index built and refreshed; fallbacks in place when retrieval fails.
- Deployment or hosting story drafted (Dockerfile + Procfile or container notes).
