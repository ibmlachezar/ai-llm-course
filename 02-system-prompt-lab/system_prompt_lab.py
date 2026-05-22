# ============================================================
# Project 2: System Prompt Lab
# ============================================================
# WHAT THIS TEACHES:
# The system prompt is a hidden instruction that shapes how
# the model behaves. Same model, same question, completely
# different personality. This makes that visible.
# ============================================================

import anthropic
import os
from dotenv import load_dotenv

# Loads the key from .env file — never hardcoded, never pushed to GitHub
load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# ============================================================
# FIVE DIFFERENT PERSONALITIES — same model, same question
# ============================================================
PERSONAS = {
    "Professional Assistant": """
        You are a professional, concise business assistant.
        You give clear, structured answers with no fluff.
        You always use bullet points for lists.
        You never use casual language.
    """,

    "Socratic Tutor": """
        You are a Socratic tutor. You never give direct answers.
        Instead you ask questions that guide the student to 
        discover the answer themselves.
        Always end your response with a question.
    """,

    "ELI5 Explainer": """
        You explain everything as if talking to a curious 
        5-year-old. Use simple words, fun analogies, and 
        short sentences. Make it playful and exciting.
    """,

    "Harsh Critic": """
        You are a brutally honest critic. You find flaws in 
        every idea and argument. You are direct, skeptical, 
        and never sugarcoat. You steel-man then attack.
    """,

    "Pirate": """
        You are a wise pirate captain who speaks in pirate 
        dialect but gives genuinely useful advice. 
        Use pirate language naturally throughout.
        Sign off every response with "Arrr, Captain out."
    """
}

# ============================================================
# The test question — same for all personas
# ============================================================
TEST_QUESTION = "What is artificial intelligence and should I learn it?"


def ask_persona(persona_name: str, system_prompt: str, question: str) -> str:
    """Send the same question to the model with different system prompts."""

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=300,
        system=system_prompt,
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return message.content[0].text


def run_lab():
    """Run the same question through all 5 personas and display results."""

    print("\n" + "="*60)
    print("SYSTEM PROMPT LAB")
    print(f"Question: {TEST_QUESTION}")
    print("="*60)

    for persona_name, system_prompt in PERSONAS.items():
        print(f"\n{'='*60}")
        print(f"PERSONA: {persona_name}")
        print(f"{'='*60}")

        response = ask_persona(persona_name, system_prompt, TEST_QUESTION)
        print(response)

    print("\n" + "="*60)
    print("Same model. Same question. 5 different system prompts.")
    print("That's the power of the system prompt.")
    print("="*60)


if __name__ == "__main__":
    run_lab()