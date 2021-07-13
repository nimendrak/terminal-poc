import os
from flask import Flask, request, Response
import subprocess

app = Flask(__name__)


@app.route("/api/shell", methods=["GET"])
def run_command(cmd_and_args, print_constantly=False, cwd=None):
    try:
        output = []
        process = subprocess.Popen(cmd_and_args,
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, cwd=cwd)

        while True:
            next_line = process.stdout.readline()
            if next_line:
                output.append(str(next_line))
                if print_constantly:
                    print(next_line)
            elif not process.poll():
                break

        error = process.communicate()[1]

        if len(output) > 0:
            result = {}
            result["output"] = process.returncode, '\n'.join(output), error

            response = make_response(result, True, 200)
            return Response(response=response, status=200, mimetype='application/json')
        else:
            response = make_response("404 Error", True, 404)
            return Response(response=response, status=200, mimetype='application/json')


except:
    response = make_response('Exception', False, 404)
    return Response(response=response, status=404, mimetype='application/json')


if __name__ == '__main__':
    app.run('0.0.0.0')
