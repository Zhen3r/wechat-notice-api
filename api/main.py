import os
from fastapi import FastAPI

import uvicorn


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=20222,
        host="0.0.0.0",
        reload=True,
        debug=True,
    )