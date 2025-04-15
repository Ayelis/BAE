import os
import time
from huggingface_hub import InferenceClient
# from transformers import pipeline

def configure_gemma_response(prompt: str) -> str:
    """Modify the prompt to encourage concise answers"""
    return (
        f"[INST] Respond in 2 sentences max. "
        f"Strictly complete within 3 seconds. "
        f"Query: {prompt} [/INST]\n"
    )

def main():
    # Configuration
    MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1" #good
    # 503 models: google/gemma-2b-it, TinyLlama/TinyLlama-1.1B-Chat-v1.0, microsoft/phi-2
    # nonsense models: gpt2

    # pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    # pipe = pipeline("text-generation", model="stabilityai/stablelm-3b-4e1t")
    # print(pipe("Your prompt", max_new_tokens=50)[0]['generated_text'])
    # print(pipe("Your prompt", max_length=100)[0]['generated_text'])

    TIMEOUT_SECONDS = 15
    MAX_TOKENS = 500  # Keeps responses short

    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        raise EnvironmentError("HUGGINGFACE_API_KEY not set in environment variables.")

    client = InferenceClient(
        model=MODEL_NAME,
        token=api_key,
        timeout=TIMEOUT_SECONDS
    )

    print("=== BAE Interactive Mode ===")
    print("Type your message (Ctrl+C to quit)\n")

    try:
        while True:
            try:
                user_input = input("You: ")
                if not user_input.strip():
                    continue

                start_time = time.time()
                response = client.text_generation(
                    configure_gemma_response(user_input),
                    max_new_tokens=MAX_TOKENS,
                    temperature=0.7,
                )

                elapsed = time.time() - start_time
                print(f"\nBAE ({elapsed:.1f}s): {response.strip()}\n")

            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"\nError: {str(e)}")
                continue

    except KeyboardInterrupt:
        print("\nSession ended.")

if __name__ == "__main__":
    main()