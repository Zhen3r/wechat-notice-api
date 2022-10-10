import os
from pathlib import Path
from loguru import logger
from dotenv import load_dotenv

this_path = Path(os.path.abspath(__file__)).parent.parent
load_dotenv(this_path/".env")

log_path = this_path/"wechat.log"
logger.add(log_path, rotation="10 MB")