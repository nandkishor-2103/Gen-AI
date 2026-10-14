
"""Configuration settings for the chatbot."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Project directory
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")

# LLM provider
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "").strip().lower()

# Ollama configuration
OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "",
)

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "")

# Chatbot system prompt
SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "",
)


def validate_config():
    required = {
        "LLM_PROVIDER": LLM_PROVIDER,
        "OLLAMA_BASE_URL": OLLAMA_BASE_URL,
        "OLLAMA_MODEL": OLLAMA_MODEL,
        "SYSTEM_PROMPT": SYSTEM_PROMPT,
    }

    missing = [key for key, value in required.items() if not value]

    if missing:
        raise ValueError(
            f"Missing configuration in .env: {', '.join(missing)}"
        )

    return None
