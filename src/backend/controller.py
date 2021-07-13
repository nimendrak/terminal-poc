from flask import Flask, request, Response, jsonify
from flask_socketio import SocketIO, emit
import subprocess


app = Flask(__name__)
app.config["SECRET KEY"] = "mykey"
app.config["DEBUG"] = True

socketio = SocketIO(app, cors_allowed_origins="*")

def shell_run():
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
                print(next_line)
                indices = [49, 63]
                parts = [next_line[i:j] for i, j in zip(indices, indices[1:] + [None])]
                # print(parts[0])
                # socketio.emit("output", "123")
                socketio.emit("output", next_line)
                socketio.sleep(2)
            elif not process.poll():
                break

    except Exception as e:
        print(e)


@socketio.on("connect")
def frontend_connection():
    print("\n*******************")
    print("Client is Connected")
    print("*******************\n")
    emit("status", "Connection Established")
    shell_run()


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
