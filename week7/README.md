
# Week 7: Next-Token Probabilities

## Aim
To inspect next-token prediction probabilities, logits, and top-K candidate tokens using Hugging Face Transformers.

## Objective
- Load a pre-trained GPT-2 model.
- Provide an input prompt.
- Extract next-token logits.
- Convert logits into probabilities using Softmax.
- Display the top 5 candidate tokens.

## Technologies Used
- Python
- PyTorch
- Hugging Face Transformers
- GPT-2 Model

## Installation

Install the required libraries:

pip install -r requirements.txt

## Execution

Run the following command:

python main.py

## Expected Output
- Input prompt
- Top 5 next-token candidates
- Probability of each candidate
- Logits of each candidate

## Result
Successfully inspected next-token logits and probabilities and displayed the top 5 candidate tokens using GPT-2.
