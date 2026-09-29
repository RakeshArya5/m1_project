import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError(
        "OPENAI_API_KEY is missing. Add it to a .env file, e.g. OPENAI_API_KEY=your_key_here"
    )

client = OpenAI(api_key=api_key)


def ask(prompt, model="gpt-4o-mini", temperature=0.0, top_p=1.0, max_tokens=150):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
    )
    text = response.choices[0].message.content
    usage_dict = {
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
    }
    return text, usage_dict