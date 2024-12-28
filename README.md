python3.10 --version

poetry env use python3.10


### Create virtual env 
    python3.13 -m venv .venv
### Activate
    source .venv/bin/activate
### Install poetry
    poetry install

### Keep the documents in the /documents folder (You can add your own documents for the training)

### Load model

python scripts/load_model.py

### Run the main method to start the service

python app/main.py

### Web ui

http://127.0.0.1:8000

Curl command

```json
curl --location --request POST 'http://127.0.0.1:8000/ask_question' \
--header 'Content-Type: application/json' \
--data-raw '{
    "question": "What is vimal jyothi?"
}'
```
