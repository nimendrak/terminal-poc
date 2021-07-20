from flask_socketio import SocketIO, emit
from flask import Flask
from flask_cors import CORS
from random import random
from threading import Thread, Event
from time import sleep

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

import subprocess

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
app.config['CORS_HEADERS'] = 'Content-Type'

socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app)

# Server functionality for receiving and storing data from elsewhere, not related to the websocket
#Data Generator Thread
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
                        socketio.emit('responseMessage', {'log': next_line})
                        sleep(self.delay)
                    elif not process.poll():
                        break
        except KeyboardInterrupt:
            # kill()
            print("Keyboard Interrupt")

    def run(self):
        self.dataGenerator()

# Handle the webapp connecting to the websocket
@socketio.on('connect')
def test_connect():
    print('Connected to websocket\n')
    emit('responseMessage', {'data': 'Connected!'})
    # need visibility of the global thread object
    global thread
    if not thread.isAlive():
        print("Starting Thread")
        thread = DataThread()
        thread.start()

@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    print('An error occured:')
    print(e)

if __name__ == '__main__':
    # socketio.run(app, debug=False, host='0.0.0.0')
    http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
