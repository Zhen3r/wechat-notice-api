# My Persional Wechat Notice API




## Installation

1. create a wechat corp account [here](https://work.weixin.qq.com/)
1. create a corp robot
1. create a `.env` file in the folder, and write:
    ```python
    CORPID = ''  # the wechat-corp-id from step1
    CORPSECRET = '***'  # the wechat-corp-secret from step1
    AGENT_ID = ***  # the robot id from step2
    API_PWD = ''  # the password for your api
    ```
1. install python dependency
    ```bash
    pip install -r ./requirements.txt
    ```


1. [optional] run in docker

    (you can change the port in compose.yml, I'm using port 20222)

    ```bash
    docker build -t wechat-api .
    docker compose up -d
    ```


## Usage

1. Run the service:

    ```bash
    python ./api/main.py
    ```
2. Send a message to yourself on http://127.0.0.1:8000/wechat?msg=YOUR_MSG&pwd=API_PWD&to_user=YOUR_WECHAT_USR_ID&type="text"


