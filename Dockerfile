FROM python:3.8.5-slim as base

RUN useradd -m app
USER app
WORKDIR /home/app

RUN pip install --user poetry==1.1.0b2

# ======= Final image =======
FROM base

COPY . /home/app/
ENV PATH /home/app/.local/bin:$PATH
ENV FLASK_APP=app.py

RUN poetry install --no-dev --no-interaction

EXPOSE 5000

CMD poetry run gunicorn --bind 0.0.0.0:5000 --workers 1 --threads 2 main:app