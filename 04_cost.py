import os
from dotenv import load_dotenv
from helpers import ask

load_dotenv()

print("=== Estimating Cost of a Call ===")

input_cost_per_1m = float(os.getenv("INPUT_COST_PER_1M", 0.15))
output_cost_per_1m = float(os.getenv("OUTPUT_COST_PER_1M", 0.60))

prompt = "Explain what an LLM is in one sentence."
text, usage = ask(prompt)

print("Response:", text)
print("Usage:", usage)

input_cost = (usage["prompt_tokens"] / 1_000_000) * input_cost_per_1m
output_cost = (usage["completion_tokens"] / 1_000_000) * output_cost_per_1m
total_cost = input_cost + output_cost

print(f"\nInput cost: ${input_cost:.6f}")
print(f"Output cost: ${output_cost:.6f}")
print(f"Total estimated cost: ${total_cost:.6f}")