import config
import requests

def get_llm_response(message: list[dict]) -> str:
    if config.LLM_PROVIDER == "ollama":
        return ask_ollama(message)

    raise RecursionError(
        f"Unsupported LLM_PROVIDER: {config.LLM_PROVIDER}, Please use ollama."
    )


def ask_ollama(messages: list[dict]) -> str:

    url = f"{config.OLLAMA_BASE_URL}/api/chat"

    payload = {
        "model": config.OLLAMA_MODEL,
        "messages": messages,
        "stream": False
    }

    try:
        response = requests.post(url=url, json=payload, timeout=120)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            f"Could not reach ollama at {config.OLLAMA_BASE_URL}"
        )
    except Exception as err:
        raise RuntimeError(
            f"Ollama request failed: {err}"
        )

    data = response.json()

    return data["message"]["content"]



