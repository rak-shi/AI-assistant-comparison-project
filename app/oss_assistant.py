from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype=torch.float32
)

chat_history = []

def generate_response(user_input):

    global chat_history

    # Add user message
    chat_history.append({
        "role": "user",
        "content": user_input
    })

    # Keep only last few messages
    messages = chat_history[-4:]

    # Create proper chat template
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    # Tokenize
    model_inputs = tokenizer(text, return_tensors="pt")

    # Generate response
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=40,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

    # Remove prompt tokens
    generated_ids = generated_ids[:, model_inputs.input_ids.shape[1]:]

    # Decode only NEW response
    response = tokenizer.decode(
        generated_ids[0],
        skip_special_tokens=True
    )

    # Save assistant reply
    chat_history.append({
        "role": "assistant",
        "content": response
    })

    return response.strip()