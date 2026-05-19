# 🔤 Project 01 — LLM Tokenizer Visualizer

## What you will learn

LLMs do not read words. They read tokens — numerical chunks
that could be a whole word, part of a word, or punctuation.
This project makes that visible.

## Key insights

- "unhappiness" = 3 tokens, not 1 word
- "2024" splits into "202" and "4"
- Non-English text uses more tokens and costs more
- Spaces are baked INTO tokens, not separate

## Setup

    python -m venv venv
    venv\Scripts\activate
    pip install tiktoken

## Run

    python tokenizer.py

## Quiz — test yourself after running this

1. What is a token in one sentence?
2. Why do LLMs struggle with math and spelling?
3. A model has 128k token context. A doc has 100k words. Does it fit?

## Concepts

| Concept | Meaning |
|---|---|
| Token | Atomic unit an LLM processes |
| Token ID | The number the model actually sees |
| Context window | Max tokens the model can hold at once |
| Tokenization cost | Why non-English text costs more |