from transformers import pipeline

## The code snippet leverages the Hugging Face Transformers library, a powerful and widely used library for Natural Language Processing (NLP) tasks. Here's an explanation of the components involved:

## What is the transformers library?
## The transformers library is developed by Hugging Face and provides pre-trained models and tools for various NLP tasks, including text classification, question answering, text generation, and more. It supports many popular transformer-based models, such as BERT, GPT, DistilBERT, and other


# Load a pre-trained model and tokenizer for question answering
qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def answer_question(question, document):
    return qa_model(question=question, context=document)
