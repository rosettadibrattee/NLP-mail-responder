from pydantic import BaseModel

class GPTParams(BaseModel):
    message: str
    context: str = ""
    prompt: str | None = None

class GPTResponse(BaseModel):
    response: str