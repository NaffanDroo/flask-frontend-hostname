import pytest
from main import create_app
import platform
import json


@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["BCRYPT_LOG_ROUNDS"] = 4
    app.config["WTF_CSRF_ENABLED"] = False

    testing_client = app.test_client()

    context = app.app_context()
    context.push()

    yield testing_client
    context.pop()


@pytest.mark.unit
def test_hostname(test_client):
    response = test_client.get('/')
    actual_hostname = platform.node()

    assert response.status_code == 200
    print(response.data)

    assert bytes(f"Front end host: {actual_hostname}", 'utf-8') in response.data
    assert bytes("Back end host: Unknown", 'utf-8') in response.data


@pytest.mark.integration
def test_hostname_real_local_backend(test_client):
    response = test_client.get('/')
    actual_hostname = platform.node()

    assert response.status_code == 200
    print(response.data)

    assert bytes(f"Front end host: {actual_hostname}", 'utf-8') in response.data
    assert bytes(f"Back end host: {actual_hostname}", 'utf-8') in response.data
