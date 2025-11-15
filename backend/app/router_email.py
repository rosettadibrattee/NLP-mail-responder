from fastapi import APIRouter, Header, HTTPException
from app.schemas import GPTParams, GPTResponse
from app.call_gpt import call_gpt

router = APIRouter()

@router.post("/response", response_model= GPTResponse)
async def generate_email_response(
    payload: GPTParams,
    oa_key: str = Header(None, alias="x-openai-key")
    ):
        
    if not oa_key:
        raise HTTPException(
            status_code=400,
            detail="Missing OpenAI API key"
        )

    reply = call_gpt(payload, oa_key)

    return GPTResponse(response=reply)
