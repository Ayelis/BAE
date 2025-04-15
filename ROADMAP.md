# BAE Roadmap

### 0.1a – “LLM Hello World”  [Complete]
**Features**  
- CLI script that sends a dynamic prompt to an AI model and prints the reply.  
**Success Criteria** 
- Returns a coherent response in < 15s.
- Error if no reply or timeout.

---

### **0.2a – "Math Stub"**  
**Features**  
- CLI math interpreter for your AI's number-crunching  
- Safe evaluation of basic arithmetic (`+, -, *, /, ()`)  
**Success Criteria**  
- `"2 + 3 * 4"` → `14`  
- `"5 / 0"` → `[Error 42]` (rejects illegal math)  
- `"import os"` → `[Error 99]` (rejects hacker nonsense)  

---

### 0.3a – “Board Stub”  
**Features**  
- Simple Python board‑engine (e.g. `python-chess`), CLI only.  
- Load initial state, apply a single move from hard‑coded JSON.  
**Success Criteria**  
- Engine accepts valid move JSON and updates state.  
- Rejects illegal moves with an error code.

---

### 0.4a – “Structured Prompts”  
**Features**  
- Wrap LLM prompts/output in a strict JSON schema (action, from, to, reasoning).  
- Validate with Pydantic; on failure, reject and retry once.  
**Success Criteria**  
- 100% of LLM replies pass schema validation in a 20‑prompt smoke test.  
- Invalid outputs trigger a retry prompt.

---

### 0.5a – “LLM ↔ Board Loop”  
**Features**  
- FastAPI endpoint that:  
  1. Sends current board FEN + history to LLM  
  2. Receives JSON move  
  3. Applies to engine, returns new FEN + move confirmation  
**Success Criteria**  
- Completes a full move cycle end‑to‑end via HTTP.  
- Illegal LLM moves are caught and returned as errors.

---

### 0.6b – “Sandbox Simulation”  
**Features**  
- Allow LLM to request N‑step lookahead: engine simulates moves, returns outcome summary.  
- Expose `/simulate?depth=N`.  
**Success Criteria**  
- LLM can call simulate; engine returns correct board states for N=1–3.  
- Simulation latency < 2 s per ply.

---

### 0.7b – “Narrative Mode”  
**Features**  
- Swap in an RPG‑style “board” (scene graph + choices).  
- LLM outputs next scene action in JSON: `{ choice, description, consequences }`.  
**Success Criteria**  
- Can drive a 3‑step narrative with consistent state updates.  
- State persisted and reflected accurately in each prompt.

---

### 1.0 – “MVP Release”  
**Features**  
- Structured JSON directives  
- Board/RPG engine loop + optional sandbox  
- Basic session memory (last 5 turns)  
**Success Criteria**  
- A user can “play” a full chess game or 5‑step RPG, with no schema failures.  
- Overall system uptime ≥ 95% under light load.

---
