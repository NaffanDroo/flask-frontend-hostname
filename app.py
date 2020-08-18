import socket
import flask
import requests
import os
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

hostname = socket.gethostname()

if __name__ != '__main__':
    import logging

    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


@app.route("/", methods=["GET"])
def home():
    return render_template(
        template_name_or_list="home.html",
        frontend_host=hostname,
        backend_host=call_backend(),
    )


def call_backend() -> str:
    url = f"{service_url()}/v1/host"
    try:
        app.logger.debug(f"Attempting to connect to the API at {url}")
        response = requests.get(url, timeout=2)
        if response.ok:
            try:
                app.logger.info(f"Successfully connected to the API: {url}")
                backend_host = response.json()["backend_host"]
                app.logger.debug(backend_host)
                return backend_host
            except IndexError as e:
                error_msg = "API didn't contain 'backend_host'"
                app.logger.error(error_msg)
                return error_msg
        else:
            app.logger.warning(
                f"Received {response.status_code} from the API: {url}, response: {response.text}"
            )
            return "Unknown"
    except requests.exceptions.ConnectionError as ce:
        app.logger.warning(
            f"Connection failed while trying to connect to the API: {url}"
        )
        return "Unknown"
    except requests.exceptions.ReadTimeout as re:
        app.logger.warning(
            f"Connection timed out while trying to connect to the API: {url}"
        )
        return "Timed out"


def namespace() -> str:
    return os.getenv("POD_NAMESPACE", "")


def service_url() -> str:
    suffix = "svc.cluster.local"
    k8s_namespace = namespace()
    if k8s_namespace:
        return f"http://backend-service.{k8s_namespace}.{suffix}"
    else:
        return "http://localhost:5000"
