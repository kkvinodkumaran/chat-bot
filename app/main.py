from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from transformers import pipeline
import os
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Load pre-trained model for QA
qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Load the document from a file
DOCUMENT_PATH = "./documents/document.txt"
with open(DOCUMENT_PATH, "r") as file:
    document = file.read()

# Initialize FastAPI app
app = FastAPI()

_APP_GLOBAL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Use absolute path to templates directory
##templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates/"))

templates = Jinja2Templates(directory=os.path.join(_APP_GLOBAL_PATH, "templates/"))

class QuestionRequest(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/")
async def read_root():
    return {"message": "Welcome to the LLM Chat Application!"}

@app.post("/ask_question")
async def ask_question(request: QuestionRequest):
    # Get the question from the user
    question = request.question

    # Use the QA model to get the answer from the document
    answer = qa_model(question=question, context=document)

    return {"question": question, "answer": answer['answer']}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app')
