import socket
import flask
from flask import jsonify, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

hostname = socket.gethostname()


@app.route('/', methods=['GET'])
def home():
    return render_template(template_name_or_list="home.html", frontend_host=hostname, backend_host=None)
