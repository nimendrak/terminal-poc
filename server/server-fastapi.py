from fastapi import FastAPI, WebSocket
from threading import Thread, Event
from time import sleep
import subprocess

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print('Accepting client connection...')

    cmd = "ping www.google.lk"

    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )

    await websocket.accept()
    while True:
        try:
            next_line = process.stdout.readline()
            if next_line:
                print(f'new log: {next_line}')
                resp = {'value': next_line}
                websocket.send_json(resp)
            elif not process.poll():
                break
        except Exception as e:
            print('error:', e)
            break
    print('Bye..')
