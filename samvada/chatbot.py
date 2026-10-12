import config
import providers

def model_name():
    if config.PROVIDER == "openai":
        return config.OPENAI_MODEL

    if config.PROVIDER == "ollama":
        return config.OLLAMA_MODEL


def check_setup():
    """Return a helpful message if something is missing in .env, otherwise None"""
    if config.PROVIDER not in ("openai", "ollama"):
        return (
            "LLM_PROVIDER is '" + config.PROVIDER + "'.\n"
            "Please set LLM_PROVIDER to openai, gemini, or ollama in the .env file."
        )

    if config.PROVIDER == "openai" and not config.OPENAI_API_KEY:
        return "OPENAI_API_KEY is missing . \n Please add your OpenAI API Key to the env file."

    if not model_name():
        return (
            "The model name for " + config.PROVIDER + " is missing.\n"
            "Please set " + config.PROVIDER.upper() + "_MODEL in the .env file."
        )


def ask_llm(message):
    if config.PROVIDER == "openai":
        return providers.ask_openai(message)
    else:
        return providers.ask_ollama(message)


def main():
    problem = check_setup()
    if problem:
        print(f"Error: {problem}")
        return

    print("=" * 40)
    print("      Simple GenAI CLI Chatbot")
    print("=" * 40)
    print("\nProviders: ", config.PROVIDER)
    print("Model: ", model_name())

    while True:
        message = input("\nYou: ").strip()

        if message in ("exit", "stop"):
            print("Good Bye!!")
            break

        if not message:
            continue

        try:
            print(f"\n Assistent: {ask_llm(message)}")
        except Exception as e:
            print(f"Sorry, the request failed: {e}")


if __name__ == "__main__":
    main()

