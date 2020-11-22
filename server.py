import os
from flask import Flask,jsonify,render_template, request, session, Response, redirect
import json
import logic.search as indexsearch
from flask import send_from_directory



app = Flask(__name__, template_folder= "")
app._static_folder = "web/static"

@app.route('/')
def index():
    return render_template("web/static/html/index.html")


@app.route('/search',methods=['POST'])
def search():
    if (not request.is_json):
        c = json.loads(request.data)['values']
    else:
        c = json.loads(request.data)
    tweets=indexsearch.search(c['query'],5)
    # print(tweets)
    json_msg = json.dumps(tweets)
    return Response(json_msg, status=201, mimetype="application/json")


if __name__ == '__main__':
    app.run(port=8080, threaded=True, host=('127.0.0.1'))