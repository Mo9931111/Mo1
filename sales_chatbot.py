from transformers import pipeline, set_seed


def main() -> None:
    """Run a simple interactive sales chatbot from the terminal."""
    generator = pipeline("text-generation", model="distilgpt2")
    set_seed(42)
    print("Sales assistant ready. Type 'exit' to quit.")
    while True:
        user_input = input("Customer: ")
        if user_input.strip().lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        prompt = (
            "You are a friendly sales assistant helping customers.\n"
            f"Customer: {user_input}\nSales Bot:"
        )
        response = generator(prompt, max_length=50, num_return_sequences=1)
        generated = response[0]["generated_text"]
        reply = generated.split("Sales Bot:")[-1].strip()
        print(f"Sales Bot: {reply}")


if __name__ == "__main__":
    main()
