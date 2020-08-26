import os

import requests
from flask import current_app


def call_backend() -> str:
    url = f"{service_url()}/v1/host"
    try:
        current_app.logger.debug(f"Attempting to connect to the API at {url}")
        response = requests.get(url, timeout=2)
        if response.ok:
            try:
                current_app.logger.info(f"Successfully connected to the API: {url}")
                backend_host = response.json()["backend_host"]
                current_app.logger.debug(backend_host)
                return backend_host
            except IndexError as e:
                error_msg = "API didn't contain 'backend_host'"
                current_app.logger.error(error_msg)
                return error_msg
        else:
            current_app.logger.warning(
                f"Received {response.status_code} from the API: {url}, response: {response.text}"
            )
            return "Unknown"
    except requests.exceptions.ConnectionError as ce:
        current_app.logger.warning(
            f"Connection failed while trying to connect to the API: {url}"
        )
        return "Unknown"
    except requests.exceptions.ReadTimeout as re:
        current_app.logger.warning(
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
