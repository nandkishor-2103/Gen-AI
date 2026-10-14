import config
import llm_client

EXIT_COMMAND = ["exit", "quit"]

def build_message(user_input: str) -> list[dict]:
    """
    Build the message list for the single question.

    Notice what is missing: the previous questions and answers. Only the system instruction
    and the current questions are sent.

    Args:
        user_input: The question the user just typed.

    Returns:
        A list with exactly two messages.

    Example:
        >>> build_message("Hello")[-1]
        {"role": 'user', 'content': 'Hello'}
    """
    return [
        {"role": "system", "content": config.SYSTEM_PROMPT},
        {"role": "user", "content": user_input},
    ]


def main() -> None:
    """Run the chat loop until the user types 'exit' or 'quit'."""
    print("Chatbot without MEMORY")
    print(f"Provider: {config.LLM_PROVIDER}")
    print("Type 'exit' or 'quit' to stop.\n")

    configuration_error = config.validate_config()
    if configuration_error:
        print(f"Configuration problem: {configuration_error}")
        return

    while True:
        try:
            user_input = input("YOU: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("RADHE RADHE!!")
            return

        if not user_input:
            print("Please type a question.\n")
            continue

        if user_input.lower() in EXIT_COMMAND:
            print("RADHE RADHE!!")
            return

        try:
            reply = llm_client.get_llm_response(build_message(user_input= user_input))
        except Exception as err:
            print(f"Sorry, something went wrong: {err}\n")
            continue

        print(f"ASSISTANT: {reply}\n")


if __name__ == "__main__":
    main()
