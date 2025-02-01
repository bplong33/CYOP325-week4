import os
import uvicorn
from fastapi import FastAPI

DOWNLOADS = os.path.realpath(os.getcwd() + '/downloads')

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Welcome to my Week 3 App!"}

@app.get('/search')
def download(filename: str):
    with open(os.path.join(DOWNLOADS, filename), 'r') as tmp:
        content = tmp.readlines()

    return {"filename": filename, "content": ''.join(content)}

def run():
    uvicorn.run("app:app", port=8080, log_level='debug')
