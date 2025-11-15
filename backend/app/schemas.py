from pydantic import BaseModel

class EmailRequest(BaseModel):
    message: str
    context: str | None = None

class EmailResponse(BaseModel):
    response: str

class GPTParams(BaseModel):
    message: str
    context: str = ""
    prompt: str = "NLP"