import os
from dotenv import load_dotenv

print("=== Setup Check ===")

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError(
        "OPENAI_API_KEY is missing. Add it to a .env file, e.g. OPENAI_API_KEY=your_key_here"
    )

print("Found OPENAI_API_KEY in .env")
print("Key starts with:", api_key[:5] + "...")
print("Setup looks good. You're ready to make API calls.")