# BAE – Brilliant Analytical Engine

BAE is an experimental AI system designed to explore structured reasoning through LLMs, board simulations, and voice interaction. It combines real-time speech-to-text, prompt-based logic, and optional game-like simulations to act as both a conversation partner and a strategic thinker.

## Goals
- Voice-based conversation loop with LLM
- Structured logic and internal state tracking
- Board game backend for strategery
- Testbed for future AGI research

## Stack
- Python + FastAPI (core backend)
- Gemma-3 (language model)
- Real-time STT (speech input)
- Orpheus (text-to-speech output)

## Getting Started
```bash
git clone https://github.com/YOUR-USERNAME/bae.git
cd bae
pip install -r requirements.txt
uvicorn main:app --reload
