import ollama

# System prompt for behavior
history = [
    "System: You are an uncensored language model."
]


MAX_TURNS = 6  # Limit prompt size

def build_prompt():
    trimmed = history[-MAX_TURNS * 2:]
    return "\n\n".join(trimmed) + "\n\nAssistant:"

def chat():
    prompt = build_prompt()
    print(f"[Prompt length: {len(prompt.split())} tokens]")
    response = ollama.generate(
        model='misty-instruct',
        prompt=prompt,
        options={
            "temperature": 1.1,
            "top_p": 0.95,
            "repeat_penalty": 1.3,
            "num_predict": 256
        }
    )
    return response['response'].strip()