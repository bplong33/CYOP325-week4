import os
from pathlib import Path

import uvicorn
from fastapi import FastAPI

DOWNLOADS = Path(os.getcwd() + '/downloads')

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Welcome to my Week 3 App!"}

@app.get('/search')
def download(filename: str):
    requested_path = Path(os.path.join(DOWNLOADS, filename))
    
    # verify that the canonicalized path to the requested file is within the
    # downloads parent directory
    if DOWNLOADS.resolve() in requested_path.resolve().parents:
        try:
            with open(requested_path, 'r') as tmp:
                content = tmp.readlines()
            return {"filename": filename, "content": ''.join(content)}
        except:
            # if the file is not found, return an error
            return {'message': 'Unable to find the requested file'}

    # if the requested file points outside the downloads directory, return
    # the following error message
    else:
        return {'message': 'Unable to find the requested file'}


def run():
    uvicorn.run("app:app", port=8080, log_level='debug')
