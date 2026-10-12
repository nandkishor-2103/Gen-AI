import config

import requests
from google import genai
from openai import OpenAI

def ask_openai(message):
    """Send one message to OpenAI and return the answer as text"""
    client = OpenAI(api_key= config.OPENAI_API_KEY)

    response = client.responses.create(
        model=config.OPENAI_MODEL,
        instructions= config.SYSTEM_PROMPT,
        input= message
    )

    return response.output_text


def ask_ollama(message):
    """Send one message to a model running locally in Ollama."""

    try:
        response = requests.post(
            config.OLLAMA_BASE_URL + "/api/chat",
            json={
                "model": config.OLLAMA_MODEL,
                "messages": [
                    {
                        "role": "system",
                        "content": config.SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                "stream": False,
            },
            timeout=120,
        )

    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Could not reach Ollama. Make sure Ollama is running."
        )

    response.raise_for_status()

    data = response.json()

    return data["message"]["content"]


