from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/')
def get():
    return {'msg': 'Hello, World.'}
