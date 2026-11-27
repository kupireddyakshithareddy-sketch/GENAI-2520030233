# Generative AI Programming Practicals 🚀

A hands-on Generative AI learning project covering Large Language Models (LLMs), API integration, tokenization, monitoring, token economics, and LLM evaluation using Python.

## 📌 Project Overview

This repository contains six weeks of Generative AI practical experiments completed using Python, VS Code, cloud-based LLM APIs, and local LLM models.

The main objective is to understand how Large Language Models work and learn how to build, integrate, monitor, and evaluate LLM-powered applications.

## 🛠️ Technologies Used

- Python
- OpenAI API
- Google Gemini API
- Ollama
- Llama 3.2
- MongoDB Atlas
- Hugging Face Transformers
- BPE, WordPiece and SentencePiece
- Requests
- Pytest / Unittest
- Visual Studio Code
- Git and GitHub

## 📚 Weekly Practical Details

### Week 1 – First LLM API Call

- Connected a Python application to an LLM using an API.
- Used OpenAI API and explored Gemini API integration.
- Managed API keys using environment variables.
- Generated AI responses from user prompts.

**Skills:** Python, API Integration, Prompting, Environment Variables.

### Week 2 – Provider-Agnostic LLM Client

- Built a common interface for different LLM providers.
- Integrated Google Gemini and local Ollama.
- Implemented a reusable LLM client.
- Performed basic unit testing.

**Skills:** Python OOP, Gemini, Ollama, API Abstraction, Unit Testing.

### Week 3 – LLM Monitoring with MongoDB

- Extended the LLM client with monitoring features.
- Captured input and output token usage.
- Measured response latency.
- Estimated API usage costs.
- Stored successful and failed request details in MongoDB.
- Implemented timeouts and retry handling.

**Skills:** MongoDB, LLM Monitoring, Token Usage, Latency Tracking, Error Handling.

### Week 4 – Tokenizer Lab

- Implemented three subword tokenization approaches.
- Compared BPE, WordPiece and SentencePiece.
- Tested English, Telugu and Hindi text.
- Compared token pieces, token IDs and token counts.

**Skills:** Hugging Face Transformers, NLP, Tokenization, Multilingual Processing.

### Week 5 – Token Economics

- Developed an LLM token budget planning tool.
- Estimated daily and monthly token consumption.
- Calculated input and output token costs.
- Checked Requests Per Minute (RPM) and Tokens Per Minute (TPM).
- Applied safety margins and budget limits.

**Skills:** Python, Cost Estimation, Token Economics, Rate-Limit Management.

### Week 6 – LLM Evaluation and Baseline Testing

- Created a golden question set containing 30 questions.
- Used Ollama with the Llama 3.2 model.
- Generated answers for each question.
- Compared generated answers against expected keywords.
- Calculated keyword coverage scores.
- Classified responses as PASS, REVIEW or ERROR.
- Exported evaluation results into a CSV file.
- Created the first baseline experiment as Release v0.1.

**Skills:** LLM Evaluation, Ollama, Llama 3.2, Python, JSON, CSV, Keyword-Based Scoring.

## 📁 Project Structure

```text
Generative-AI-Practicals/
│
├── week1/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── week2/
│   ├── main.py
│   ├── llm_client.py
│   ├── test_client.py
│   └── requirements.txt
│
├── week3/
│   ├── main.py
│   ├── llm_client.py
│   ├── usage_logger.py
│   ├── test_client.py
│   └── requirements.txt
│
├── week4/
│   ├── tokenizer_comparison.py
│   └── requirements.txt
│
├── week5/
│   ├── budget.py
│   ├── test_budget.py
│   └── requirements.txt
│
├── week6/
│   ├── main.py
│   ├── golden_set.json
│   ├── requirements.txt
│   └── baseline_results.csv
│
├── .gitignore
└── README.md
```

*Note: The folder and file names above illustrate the project organization. Keep your actual filenames and folders as they are in your repository.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd Generative-AI-Practicals
```

### 3. Create a virtual environment

```bash
python -m venv .myenv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.\.myenv\Scripts\Activate.ps1
```

### 5. Install dependencies

Open the required weekly folder and run:

```bash
pip install -r requirements.txt
```

### 6. Run the practical

For example, Week 6:

```bash
cd week6
python main.py
```

Note: Configure the required API keys, MongoDB connection and Ollama model for the respective practicals.

## 🔐 Security

- API keys are stored in `.env` files.
- Sensitive credentials should never be uploaded to GitHub.
- Virtual environment folders should not be committed.
- MongoDB credentials must remain private.

## 🎯 Learning Outcomes

Through these six practicals, I gained hands-on experience in:

- Integrating LLM APIs with Python.
- Working with cloud and local language models.
- Building reusable LLM applications.
- Monitoring token usage, latency and cost.
- Understanding multilingual tokenization.
- Estimating LLM application budgets.
- Evaluating LLM responses using a golden dataset.

## 👩‍💻 Author

**K. Akshitha Reddy**

Generative AI | Python | LLM Applications | NLP | MongoDB

---

⭐ This repository represents my hands-on learning journey in Generative AI Programming.
