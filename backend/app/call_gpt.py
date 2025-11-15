from openai import OpenAI
from app.config import OPENAI_API_KEY as oa_key
from app.constants import GPT_PROMPTS
from app.schemas import GPTParams

client = OpenAI(api_key= oa_key)

def call_gpt(params: GPTParams) -> str:
    message = params.message
    context = params.context
    
    # Defaults to "NLP", but can be extended for other prompts
    prompt = params.prompt  
    
    vaiables = {
        "message": message,
        "context": context, 
    }
    
    completion = client.responses.create(
        prompt={
            "id": GPT_PROMPTS[prompt],
            "variables": vaiables
        }
    )
    
    return completion.output_text
