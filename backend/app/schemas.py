from pydantic import BaseModel

class GPTParams(BaseModel):
    message: str
    context: str = ""
    prompt: str = "NLP"

class GPTResponse(BaseModel):
    response: str