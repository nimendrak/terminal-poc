FROM python:3.7

WORKDIR /backend/

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD uvicorn server-fastapi.py:app