
from fastapi import FastAPI

app = FastAPI(title="Enterprise RAG Chatbot")

@app.get("/")
def home():
    return {"message": "RAG Chatbot Running"}
