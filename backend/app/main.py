from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router_email import router as email_router

app = FastAPI(
    title="NLP Email Responder API",
    version="1.0.0",
    description="Backend service that analyzes incoming emails using NLP and generates contextual replies via GPT."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # to restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(email_router, prefix="/api/v1")

@app.get("/", tags=["Health"])
async def root():
    return {"status": "ok", "message": "NLP Email Responder API is running"}
