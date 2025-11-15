# 🧠 NLP Message Responder
### _Context-aware AI replies for any message. Full-stack, production-ready._

A minimal but complete AI tool that analyzes any incoming **message** (email, DM, support request, negotiation, complaint, etc.) using NLP, then generates a polished, context-appropriate response.

Built end-to-end with:

- **FastAPI** (backend, OpenAI integration)
- **Vue 3 + Vite** (frontend UI)
- **OpenAI GPT-4o** (NLP + response generation)
- **Render** (backend hosting)
- **Vercel** (frontend hosting)

This project demonstrates real full-stack execution: backend design, frontend UX, AI prompting, deployment, and product structure.

---

## 🚀 Features

### 🔍 NLP-Driven Message Analysis  
The backend uses a structured OpenAI prompt to:
- Detect intent  
- Extract sentiment  
- Parse contextual hints  
- Understand subtext  
- Produce tailored, human-sounding replies  

### ✍️ Generate Context-Aware Responses  
Paste any message → Receive a clean, ready-to-send reply.

### 🔐 Local OpenAI Key Storage  
No backend storage.  
User API keys are stored **securely in localStorage**—never transmitted or logged by the backend.

### ⚙️ Dedicated Settings Screen  
Includes:
- API key input  
- Key validation (verified with OpenAI before saving)  
- “Show/hide key” eye toggle  

### 💡 Clean, Fast Frontend  
Vue 3 + Vite with:
- Router navigation  
- Simple two-page UX  
- Minimal, focused UI  
- Default NLP mode (no tone selection needed)  

### 🌐 Production Deployment  
- **Backend → Render**  
- **Frontend → Vercel**  
- CORS-ready  
- Zero backend secrets from the user

---

## 🧩 Tech Stack
### **Frontend**
- Vue 3  
- Vite  
- Vue Router  
- LocalStorage (API key)  

### **Backend**
- FastAPI  
- Pydantic  
- OpenAI responses API  
- Render deployment  

### **AI**
- OpenAI GPT-4o  
- Prompt templates stored on backend  
- Structured NLP-driven reply engine  

### **Deployment**
- Vercel (frontend)  
- Render (backend)

---

## 📦 Project Structure
```txt
NLP-message-responder/
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── schemas.py
│ │ ├── call_gpt.py
│ │ ├── router_email.py
│ │ ├── constants.py
│ │ └── config.py
│ ├── pyproject.toml
│ └── requirements.txt
└── frontend/
├── src/
│ ├── App.vue # root router shell
│ ├── Home.vue # main responder page
│ ├── Settings.vue # API key management
│ ├── router.js
│ └── composables/
│ │ └── useSettings.js
├── main.css
└── vite.config.js
```

⚙️ Backend Setup
```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

Run locally:
```bash
uvicorn app.main:app --reload
```

API available at:
```
http://localhost:10000/api/response
```

🎨 Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Set backend URL inside your frontend .env:
VITE_API_URL=http://localhost:10000/api

🌍 Deployment
Backend → Render
Deploy /backend

Render will expose your public API endpoint
Frontend → Vercel
Deploy /frontend
Add API_URL in Vercel environment variables

🧠 How It Works
User pastes an email
 -> Selects the tone
 -> Frontend sends data to /api/respond
 -> FastAPI composes an NLP prompt
 -> OpenAI generates the email reply
 -> Response returned instantly

📜 License
MIT 
