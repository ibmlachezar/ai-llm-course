# 🎭 Project 02 — System Prompt Lab

## What you will learn

The system prompt is a hidden instruction that shapes how the
model behaves. Same model, same question, five completely
different personalities. This project makes that visible.

## Key insights

- Base model vs assistant model — same knowledge, different behavior
- System prompt = developer instructions the user never sees
- Personality, boundaries, format and identity all controlled here
- No retraining needed — just words in a text field

## Setup

    python -m venv venv
    venv\Scripts\activate
    pip install anthropic python-dotenv

    cp .env.example .env
    # Add your Anthropic API key to .env

## Run

    python system_prompt_lab.py

## What it does

Sends the same question to Claude 5 times with different
system prompts — Professional, Socratic, ELI5, Harsh Critic,
and Pirate. Shows how dramatically behavior changes.

## Quiz — test yourself

1. What is the difference between a base model and assistant model?
2. Where do you put behavioral instructions for a chatbot?
3. Can users see the system prompt?
4. Name 3 things you can control with a system prompt.

## Concepts

| Concept | Meaning |
|---|---|
| Base model | Raw prediction model trained on internet data |
| Assistant model | Base model fine-tuned to be helpful and safe |
| System prompt | Hidden developer instruction before every conversation |
| RLHF | How base models become assistant models — see Project 10 |