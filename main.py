import os
from huggingface_hub import InferenceClient

# Grab token from env
api_key = os.getenv("HUGGINGFACE_API_KEY")
if not api_key:
    raise EnvironmentError("HUGGINGFACE_API_KEY not set in environment variables.")

# Init client
client = InferenceClient(
    model="gpt2",
    token=api_key
)

# Prompt
prompt = "Write a short story about a robot that learns to garden."

# Generate
response = client.text_generation(
    prompt,
    max_new_tokens=100,
    temperature=0.7,
)

print(response)
