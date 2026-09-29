import tiktoken

print("=== Token Counting with tiktoken ===")

encoding = tiktoken.get_encoding("o200k_base")

sentences = [
    "Hi.",
    "Large language models predict the next token.",
    "Tokenization splits text into smaller pieces called tokens before a model can process it.",
    "Supercalifragilisticexpialidocious is a fun, unusually long word to tokenize!",
]

for sentence in sentences:
    tokens = encoding.encode(sentence)
    print(f"\nSentence: {sentence}")
    print("Token count:", len(tokens))

print("\n=== Token-by-token preview (first sentence with more length) ===")
sample = sentences[3]
tokens = encoding.encode(sample)[:20]
for token_id in tokens:
    piece = encoding.decode([token_id])
    print(f"{token_id} -> '{piece}'")