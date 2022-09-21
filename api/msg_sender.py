import os
from .utils import logger, this_path
import requests
import pandas as pd

CORPID = os.getenv("CORPID")
CORPSECRET = os.getenv("CORPSECRET")

def send_wechat_msg(user, msg):
    ...


def get_access_token():
    ...
    saved_tokens = pd.read_csv(this_path/"saved_tokens.csv")
    t, token = saved_tokens.tail(1).values
    (pd.Timestamp.now()- t).seconds