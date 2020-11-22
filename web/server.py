import os
from flask import Flask,jsonify,render_template, request, session, Response, redirect
import json


app = Flask(__name__, template_folder= "static/html")


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/search',methods=['POST'])
def search():
    if (not request.is_json):
        c = json.loads(request.data)['values']
    else:
        c = json.loads(request.data)
    print(c)
    message = {'msg': 'mensajeserver'}
    json_msg = json.dumps(message)
    return Response(json_msg, status=201, mimetype="application/json")


if __name__ == '__main__':
    app.run(port=8080, threaded=True, host=('127.0.0.1'))