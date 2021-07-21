from fastapi import FastAPI, WebSocket
from threading import Thread, Event
from time import sleep
import subprocess

app = FastAPI()

# Server functionality for receiving and storing data from elsewhere, not related to the websocket
# Data Generator Thread
thread = Thread()

thread_stop_event = Event()


class DataThread(Thread):
    def __init__(self):
        self.delay = 1
        super(DataThread, self).__init__()

    def dataGenerator(self):
        print("Initialising")
        try:
            while not thread_stop_event.isSet():
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
                        # socketio.emit('responseMessage', {'log': next_line})
                        sleep(self.delay)
                    elif not process.poll():
                        break
        except KeyboardInterrupt:
            # kill()
            print("Keyboard Interrupt")

    def run(self):
        self.dataGenerator()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/", operation_id="1")
async def read_items():
    return [{"item_id": "Foo"}]


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print('Accepting client connection...')
    await websocket.accept()
    while True:
        try:
            # Send message to the client
            resp = {'value': "connected"}
            await websocket.send_json(resp)
            global thread
            if not thread.isAlive():
                print("Starting Thread")
                thread = DataThread()
                thread.start()
        except Exception as e:
            print('error:', e)
            break
    print('Bye..')
