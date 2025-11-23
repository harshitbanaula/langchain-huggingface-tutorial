 ## LangChain HuggingFace AI Examples

This project demonstrates how to use **LangChain with Hugging Face** for:

- 🔹 Chat-based LLM interactions (Mistral-7B)
- 🔹 Generating embeddings using Sentence Transformers
- 🔹 Managing API keys securely with `.env`

This project is beginner-friendly and useful for learning AI model operations in Python.

---

## 📁 Project Structure
HF_Tutorial/
│
├── src/
│ ├── chat_models/
│ │ └── main.py # Chat model using Mistral-7B Instruct
│ ├── embedding_models/
│ │ └── embed.py # Text embedding example
│
├── .env # Stores HuggingFace API key (not committed)
├── .gitignore # Keeps .env & venv hidden
├── requirements.txt # Dependencies
└── README.md # This documentation

yaml
Copy code

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/<your-username>/langchain-huggingface-tutorial.git
cd langchain-huggingface-tutorial
2️⃣ Create & Activate Virtual Environment
sh
Copy code
python -m venv .venv

# Windows:
.venv\Scripts\activate

# Mac/Linux:
source .venv/bin/activate
3️⃣ Install Dependencies
sh
Copy code
pip install -r requirements.txt
4️⃣ Add Hugging Face API Key
Create a .env file in the project root:

ini
Copy code
HUGGINGFACEHUB_API_TOKEN=your_api_key_here
🧪 Run Examples
➡ Embedding Example

sh
Copy code
python src/embedding_models/embed.py
➡ Chat Model Example

sh
Copy code
python src/chat_models/main.py
🛠 Tech Stack
Feature	Library Used
Embeddings	Sentence Transformers
Text Generation	HuggingFace Inference API
LLM Framework	LangChain
Env Management	python-dotenv

🔐 Security Notes
✔ .env is ignored using .gitignore
✔ Do not upload API keys to GitHub

👤 Author
Harshit Banaula
