from helpers import ask

print("=== Temperature Comparison ===")

prompt = "Describe what a context window is in 2 sentences."

print("\n--- temperature=0.0, run 1 ---")
text, usage = ask(prompt, temperature=0.0)
print(text)

print("\n--- temperature=0.0, run 2 ---")
text, usage = ask(prompt, temperature=0.0)
print(text)

print("\n--- temperature=0.9, run 1 ---")
text, usage = ask(prompt, temperature=0.9)
print(text)

print("\n--- temperature=0.9, run 2 ---")
text, usage = ask(prompt, temperature=0.9)
print(text)