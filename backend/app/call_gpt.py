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
    
    payload = f"""
    Input:
    {message}

    Context:
    {context}
    """.strip()
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        prompt_id=GPT_PROMPTS[prompt],
        messages=[
            {
                "role": "user",
                "content": payload,
            }
        ],
        max_tokens=300,
        temperature=0.4
    )
    return completion.choices[0].message.content.strip()
