from fastapi import APIRouter
from app.schemas import EmailRequest, EmailResponse, GPTParams
from app.call_gpt import call_gpt

router = APIRouter()

@router.post("/response", response_model=EmailResponse)
async def generate_email_response(payload: EmailRequest):

    params = GPTParams(
        message=payload.message,
        context=payload.context or "",
        prompt=payload.prompt  # defaults to "NLP" automatically
    )

    reply = call_gpt(params)

    return EmailResponse(response=reply)
