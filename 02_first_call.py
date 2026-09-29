from helpers import ask

print("=== First API Call ===")

prompt = "Explain what an LLM is in one sentence."
text, usage = ask(prompt)

print("Prompt:", prompt)
print("Response from LLM:", text)
print("Usage:", usage)