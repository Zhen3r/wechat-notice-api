import os
from utils import logger
import time
import requests

CORPID = os.getenv("CORPID")
CORPSECRET = os.getenv("CORPSECRET")
TOKEN_TIMEOUT = 6000


class WechatUtils():
    def __init__(self) -> None:
        self._token_time = 1663856982.597988
        # self.__token = None
        self.__token = "9ddD4GuzJ9sqd2sXg005q-E8sKfcFx_z7Qa1b85KHszLTHSDVEB84ry9b-bHUBL8sPEmhC4uGjwwLawMZx1vhhK3IrBTfTmPqMgmaCOHzEhVae6bS7Rn2nEXEbKEB2X5ofYSsF3GdjNpYWksp_jIPJp4xggSvsvpgMSWPs9HZ-NoKbwdOypi8yuM_BJ9JevgE76vWgxZlyO64L-A17SDQg"

    def send_text_msg(self, msg, user="1"):
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send"
        params = {"access_token": self._token}
        data = {
            "touser": user,
            "msgtype": "text",
            "agentid": 1000002,
            "text": {
                "content": msg,
            },
            "duplicate_check_interval": 10,
            "debug": 1,
        }
        resp = requests.post(url, params=params, json=data).json()
        return resp

    def _get_new_access_token(self):
        logger.info("Obtaining new access token!")
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {"corpid": CORPID, "corpsecret": CORPSECRET}
        resp = requests.get(url, params=params).json()
        if resp["errcode"] != 0:
            logger.error(str(resp))
        return time.time(), resp["access_token"]

    @property
    def _token(self):
        now = time.time()
        if now - self._token_time >= TOKEN_TIMEOUT:
            self._token_time, self.__token = self._get_new_access_token()
        print(self.__token)
        return self.__token


if __name__ == "__main__":
    print(WechatUtils().send_text_msg("你的快递到了"))
