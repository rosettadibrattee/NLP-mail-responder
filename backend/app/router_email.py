from fastapi import APIRouter
from app.schemas import GPTParams, GPTResponse
from app.call_gpt import call_gpt

router = APIRouter()

@router.post("/response", response_model= GPTResponse)
async def generate_email_response(payload: GPTParams):

    params = GPTParams(
        message=payload.message,
        context=payload.context,
        prompt=payload.prompt
    )

    reply = call_gpt(params)

    return GPTResponse(response=reply)
