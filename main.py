from flask import Flask

from blueprints.hostname import hostname


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.register_blueprint(hostname)
    return app


app = create_app()

if __name__ != '__main__':
    import logging

    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
