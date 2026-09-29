from helpers import ask

print("=== Hallucination Demo ===")

question = "What does the 'Flexnorm Coefficient' mean in machine learning?"

print("\n--- before (no safety rule) ---")
before_text, before_usage = ask(question)
print(before_text)

print("\n--- after (with a safety rule) ---")
safe_question = (
    question
    + " If you cannot verify this, respond exactly: Not found."
)
after_text, after_usage = ask(safe_question)
print(after_text)