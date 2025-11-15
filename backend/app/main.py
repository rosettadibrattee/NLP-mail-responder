from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router_email import router as email_router

app = FastAPI(
    title="NLP Mail Responder API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # to limit later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "nlp-mail-responder",
        "docs": "/docs",
    }


@app.get("/healthz")
async def health_check():
    return {"status": "ok"}

app.include_router(email_router, prefix="/api")
