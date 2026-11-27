
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load GPT-2 model
model_name = "openai-community/gpt2"

print("Loading GPT-2 model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Input prompt
prompt = "Artificial Intelligence is"

print("\nInput Prompt:", prompt)

# Tokenize the input
inputs = tokenizer(prompt, return_tensors="pt")

# Get model output
with torch.no_grad():
    outputs = model(**inputs)

# Get next-token logits
logits = outputs.logits[:, -1, :]

# Convert logits into probabilities
probabilities = torch.softmax(logits, dim=-1)

# Get top 5 predictions
top_k = 5
top_probs, top_indices = torch.topk(probabilities, top_k)

print("\nTop 5 Next Token Candidates:\n")

for i in range(top_k):
    token_id = top_indices[0][i].item()
    token = tokenizer.decode([token_id])
    probability = top_probs[0][i].item()

    print("Token:", repr(token))
    print("Probability:", round(probability, 6))
    print()

# Display logits
print("Top 5 Next Token Logits:\n")

for i in range(top_k):
    token_id = top_indices[0][i].item()
    token = tokenizer.decode([token_id])
    logit = logits[0][token_id].item()

    print("Token:", repr(token))
    print("Logit:", round(logit, 4))
    print()
