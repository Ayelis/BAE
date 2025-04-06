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
git clone https://github.com/ayelis/bae.git
python -m venv venv
.\venv\Scripts\activate         # Or `source venv/bin/activate` on *nix
pip install -r requirements.txt # if you've added one
py main.py                      # Run your script
