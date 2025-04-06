# BAE Roadmap

### 0.1a – “LLM Hello World”  
**Features**  
- CLI script that sends a hard‑coded prompt to Gemma‑3 and prints the reply.  
**Success Criteria**  
- Returns a coherent response in < 3s.  
- Error if no reply or timeout.

---

### 0.2a – “API Wrapper”  
**Features**  
- FastAPI service exposing `/chat` that proxies requests to your LLM.  
**Success Criteria**  
- `POST /chat` returns LLM output with HTTP 200.  
- Handles 5 concurrent requests without crashing.

---

### 0.3a – “Hear Me”  
**Features**  
- Integrate real‑time STT: record a short WAV, transcribe to text, feed `/chat`.  
**Success Criteria**  
- Transcription accuracy ≥ 90% on a 10‑phrase test set.  
- End‑to‑end: speak → text → LLM reply.

---

### 0.4a – “Speak Back”  
**Features**  
- Hook Orpheus TTS to `/chat` responses and play audio.  
**Success Criteria**  
- Audio plays with < 1 s latency after text arrives.  
- Voice clarity acceptable on test sentences.

---

### 0.5a – “Board Stub”  
**Features**  
- Simple Python board‑engine (e.g. `python-chess`), CLI only.  
- Load initial state, apply a single move from hard‑coded JSON.  
**Success Criteria**  
- Engine accepts valid move JSON and updates state.  
- Rejects illegal moves with an error code.

---

### 0.6a – “Structured Prompts”  
**Features**  
- Wrap LLM prompts/output in a strict JSON schema (action, from, to, reasoning).  
- Validate with Pydantic; on failure, reject and retry once.  
**Success Criteria**  
- 100% of LLM replies pass schema validation in a 20‑prompt smoke test.  
- Invalid outputs trigger a retry prompt.

---

### 0.7a – “LLM ↔ Board Loop”  
**Features**  
- FastAPI endpoint that:  
  1. Sends current board FEN + history to LLM  
  2. Receives JSON move  
  3. Applies to engine, returns new FEN + move confirmation  
**Success Criteria**  
- Completes a full move cycle end‑to‑end via HTTP.  
- Illegal LLM moves are caught and returned as errors.

---

### 0.8a – “Sandbox Simulation”  
**Features**  
- Allow LLM to request N‑step lookahead: engine simulates moves, returns outcome summary.  
- Expose `/simulate?depth=N`.  
**Success Criteria**  
- LLM can call simulate; engine returns correct board states for N=1–3.  
- Simulation latency < 2 s per ply.

---

### 0.9a – “Narrative Mode”  
**Features**  
- Swap in an RPG‑style “board” (scene graph + choices).  
- LLM outputs next scene action in JSON: `{ choice, description, consequences }`.  
**Success Criteria**  
- Can drive a 3‑step narrative with consistent state updates.  
- State persisted and reflected accurately in each prompt.

---

### 1.0 – “MVP Release”  
**Features**  
- Full voice I/O (STT ↔ LLM ↔ TTS)  
- Structured JSON directives  
- Board/RPG engine loop + optional sandbox  
- Basic session memory (last 5 turns)  
**Success Criteria**  
- A user can “play” a full chess game or 5‑step RPG via voice only, with no schema failures.  
- Overall system uptime ≥ 95% under light load.

---
