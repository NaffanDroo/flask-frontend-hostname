import socket

from flask import Blueprint, render_template

from backend.backend import call_backend

hostname = Blueprint('hostname', __name__)


@hostname.route("/", methods=["GET"])
def home():
    host = socket.gethostname()
    return render_template(
        template_name_or_list="home.html",
        frontend_host=host,
        backend_host=call_backend(),
    )
