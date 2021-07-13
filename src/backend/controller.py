import os
from flask import Flask, request, Response, Api
from flask_socketio import SocketIO, send

from util import make_response
import subprocess


app = Flask(__name__)
app.config['SECRET KEY'] = "mykey"
app.config["DEBUG"] = True
api = Api(app)

socketio = SocketIO(app, cors_allowed_origins="*")

def shell_run():
    cmd = "ping www.google.lk"

    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)

    while True:
        next_line = process.stdout.readline()
        if next_line:
            socketio.emit('shell output', next_line)
        elif not process.poll():
            break

    emit("newdata", {"td": sample}, namespace="/home")
    socketio.sleep(1)

@socketio.on("connect", namespace="/shell")
def frontend_connection():
  print("Client is Connected")
  shell_run()


# @app.route("/api/shell/<cmd>", methods=["GET"])
# def run_command(cmd, print_constantly=False, cwd=None):
#     try:
#         output = []
#         process = subprocess.Popen(cmd,
#                                    shell=True,
#                                    stdout=subprocess.PIPE,
#                                    stderr=subprocess.PIPE,
#                                    universal_newlines=True)

#         while True:
#             next_line = process.stdout.readline()
#             if next_line:
#                 output.append(str(next_line))
#                 if print_constantly:
#                     print(next_line)
#             elif not process.poll():
#                 break

#         error = process.communicate()[1]

#         if len(output) > 0:
#             result = {}
#             result["output"] = process.returncode, '\n'.join(output), error

#             response = make_response(result, True, 200)
#             return Response(response=response, status=200, mimetype='application/json')
#         else:
#             response = make_response("404 Error", True, 404)
#             return Response(response=response, status=200, mimetype='application/json')

#     except Exception as e:
#         response = make_response("Exception - {}".format(e), False, 500)
#         return Response(response=response, status=500, mimetype='application/json')


if __name__ == '__main__':
    socketio.run(app)
