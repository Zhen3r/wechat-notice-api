FROM python:3.9.12

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple/

COPY . ./
CMD [ "python", "./api/main.py" ]
EXPOSE 8000
