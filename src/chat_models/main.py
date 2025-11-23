from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Replace with your actual Hugging Face API token

# Create the endpoint with your API key
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    max_new_tokens=100,
    temperature=0.5,
    top_p=0.95,
)

# Wrap in ChatHuggingFace for conversational interface
chat_model = ChatHuggingFace(llm=llm)

# Test the model
response = chat_model.invoke(" can you tell me about yourself..")
print(response)
