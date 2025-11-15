# NLP-mail-responder
“AI Email Responder built with FastAPI and Vue. Paste an email, choose a tone, and generate a polished, ready-to-send reply using OpenAI. Fully deployable demo showcasing full-stack development, AI integration, and end-to-end product execution.

📨 AI Email Responder

A minimal, full-stack AI tool that generates clean, ready-to-send email replies. Built with FastAPI, Vue 3, and OpenAI GPT-4o-mini. Designed to demonstrate end-to-end product execution: backend, frontend, AI integration, and deployment.

🚀 Features

Paste any email and generate a polished reply
Tone control (formal, concise, friendly, assertive, empathetic)
- Clean, fast Vue UI
- FastAPI backend with OpenAI integration
- CORS-ready and production-deployable
- Copy-to-clipboard response
- Simple, focused UX for maximum clarity

🧩 Tech Stack

Frontend: Vue 3 + Vite
Backend: FastAPI (Python)
AI: OpenAI GPT-4o-mini
Deployment: Vercel (frontend), Fly.io (backend)

📦 Project Structure

```txt
ai-email-responder/
 ├── backend/
 │   ├── app/
 │   │   ├── main.py
 │   │   ├── router_email.py
 │   │   ├── schemas.py
 │   │   └── config.py
 │   ├── requirements.txt
 └── frontend/
     └── (Vue app)
```

⚙️ Backend Setup
cd backend
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt


Create .env:
OPENAI_API_KEY=your_key_here


Run locally:
uvicorn app.main:app --reload

API available at:
http://localhost:10000/api/response

🎨 Frontend Setup
cd frontend
npm install
npm run dev

Set backend URL inside your frontend .env:
VITE_API_URL=http://localhost:10000/api

🌍 Deployment
Frontend: Deploy /frontend on Vercel
Backend: Deploy /backend to Fly.io
Add OPENAI_API_KEY to Fly.io secrets
Update VITE_API_URL in Vercel environment variables

🧠 How It Works
User pastes an email
 -> Selects the tone
 -> Frontend sends data to /api/respond
 -> FastAPI composes an NLP prompt
 -> OpenAI generates the email reply
 -> Response returned instantly

📜 License
MIT 
