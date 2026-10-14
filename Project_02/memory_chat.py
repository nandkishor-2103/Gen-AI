import config
import llm_client
import memory

EXIT_COMMAND = ["exit", "quit"]

def build_messages(user_input: str) -> list[dict]:
    messages = [{"role": "system", "content": config.SYSTEM_PROMPT}]
    messages.extend(memory.get_history())
    messages.append({"role": "user", "content": user_input})

    return messages

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
            reply = llm_client.get_llm_response(build_messages(user_input= user_input))
        except Exception as err:
            print(f"Sorry, something went wrong: {err}\n")
            continue

        # Only now, after a successful reply, do we remember this exchange.
        memory.add_user_message(user_input)
        memory.add_assistant_message(reply)

        print(f"ASSISTANT: {reply}\n")



if __name__ == "__main__":
    main()
