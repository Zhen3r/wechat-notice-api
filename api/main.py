import os
from typing import Optional
from fastapi import FastAPI
import utils
from msg_sender import WechatUtils
import uvicorn

PWD = os.environ["API_PWD"]

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/wechat")
def send_wechat_msg(
    msg: str, 
    pwd: str,
    to_user: Optional[str] = "1",
    type: Optional[str] = "text",
):
    if not pwd==PWD: return {"detail":"Wrong pwd."}
    if type == "text":
        return WechatUtils().send_text_msg(msg, user=to_user)
    else:
        return {"detail": "type not supported"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=20222,
        host="0.0.0.0",
        reload=True,
        debug=True,
    )