from fastapi import FastAPI, WebSocket
from time import sleep
import subprocess

app = FastAPI()


@app.websocket("/shell")
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
            while True:
                next_line = process.stdout.readline()
                if next_line:
                    # Send message to the client
                    resp = {'value': next_line}
                    await websocket.send_json(resp)

                    # Print to terminal
                    print(resp)

                    # Take a break before next line is sent
                    sleep(0.5)
                    
                elif not process.poll():
                    break
            break

        except Exception as e:
            print('error:', e)
            break
        
    print('Connection interrupted..')
