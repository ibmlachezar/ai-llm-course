# ============================================================
# Project 1: LLM Tokenizer Visualizer
# ============================================================
# WHAT THIS TEACHES:
# LLMs don't see words — they see tokens (number IDs).
# This script shows exactly how any text gets broken down
# before an LLM ever processes it.
# ============================================================

import tiktoken

# We use cl100k_base — the encoding used by GPT-4 and Claude
# It has a vocabulary of 100,000 possible tokens
ENCODING = tiktoken.get_encoding("cl100k_base")

# Cost per 1000 tokens (Claude Sonnet approximate input cost)
COST_PER_1K_TOKENS = 0.003


def tokenize(text: str) -> dict:
    """
    Takes any text string and returns:
    - The tokens (as readable text chunks)
    - The token IDs (the numbers the model actually sees)
    - Token count
    - Estimated cost
    """
    token_ids = ENCODING.encode(text)

    token_chunks = [
        ENCODING.decode([tid]) for tid in token_ids
    ]

    cost = (len(token_ids) / 1000) * COST_PER_1K_TOKENS

    return {
        "text": text,
        "token_chunks": token_chunks,
        "token_ids": token_ids,
        "token_count": len(token_ids),
        "estimated_cost_usd": round(cost, 6)
    }


def display(result: dict):
    """Prints a clear, visual breakdown of the tokenization."""

    print("\n" + "="*60)
    print("INPUT TEXT:")
    print(f"  {result['text']}")

    print("\nTOKEN BREAKDOWN:")
    for i, (chunk, tid) in enumerate(
        zip(result['token_chunks'], result['token_ids'])
    ):
        display_chunk = chunk.replace('\n', '\\n')
        print(f"  [{i+1}] '{display_chunk}' → ID: {tid}")

    print(f"\nTOTAL TOKENS : {result['token_count']}")
    print(f"TOTAL WORDS  : {len(result['text'].split())}")
    print(f"TOKENS/WORD  : "
          f"{result['token_count']/max(len(result['text'].split()),1):.2f}")
    print(f"EST. COST    : ${result['estimated_cost_usd']}")
    print("="*60)


if __name__ == "__main__":

    tests = [
        "Hello, how are you?",
        "unhappiness",
        "def hello_world():",
        "The year is 2024",
        "Bonjour, comment allez-vous?",
    ]

    for text in tests:
        result = tokenize(text)
        display(result)