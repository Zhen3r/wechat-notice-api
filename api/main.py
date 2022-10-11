import os
from typing import Optional
from fastapi import FastAPI, Request
from msg_sender import WechatUtils
from utils import logger
import uvicorn

PWD = os.environ["API_PWD"]

app = FastAPI()
wechat_util = WechatUtils()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/wechat")
def send_wechat_msg(
    msg: str, 
    pwd: str,
    request: Request,
    to_user: Optional[str] = "1",
    type: Optional[str] = "text",
):
    logger.info(f"Getting an [{type}] API request from {request.client.host} to user {to_user}!")
    if not pwd==PWD: return {"detail":"Wrong pwd."}
    if type == "text":
        return wechat_util.send_text_msg(msg, user=to_user)
    else:
        return {"detail": "type not supported"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8000,
        host="0.0.0.0",
        reload=True,
        debug=True,
    )