FROM python:3.8-slim-buster

RUN pip install pipenv

COPY Pipfile* /tmp/

RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /app

COPY . .

RUN python -m pip install -e .

CMD ["python", "src.py"]