from openai import OpenAI
#from app.config import OPENAI_API_KEY as oa_key
from app.constants import GPT_PROMPTS
from app.schemas import GPTParams

def call_gpt(params: GPTParams, oa_key: str) -> str:
    client = OpenAI(api_key= oa_key)
    message = params.message
    context = params.context

    # Defaults to "NLP", but can be extended for other prompts
    prompt = params.prompt or "NLP"
    
    vaiables = {
        "context": context
    }
    
    completion = client.responses.create(
        input = message,
        prompt={
            "id": GPT_PROMPTS[prompt],
            "variables": vaiables
        }
    )
    
    return completion.output_text
