from fastapi import FastAPI, WebSocket
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
            # cmd = "seq 1 20"
            cmd = "ping www.google.lk"

            process = subprocess.Popen(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )

            while True:
                next_line = process.stdout.readline()
                if next_line:
                    print(f'new log: {next_line}')
                    # Send message to the client
                    resp = {'value': next_line}
                    await websocket.send_json(resp)

                elif not process.poll():
                    break
                break

        except Exception as e:
            print('error:', e)
            break
    print('Connection interrupted..')
