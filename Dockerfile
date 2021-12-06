FROM python:3.8-slim-buster

RUN pip install pipenv

COPY Pipfile* /tmp/

RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt

RUN pip install -r /tmp/requirements.txt
              
ENV DEVELOPER_EMAIL_COC_API     ${DEVELOPER_EMAIL_COC_API}
ENV DEVELOPER_PASSWORD_COC_API  ${DEVELOPER_PASSWORD_COC_API}
ENV DISCORD_BOT_TOKEN           ${DISCORD_BOT_TOKEN}

WORKDIR /app

COPY . .

RUN python -m pip install -e .

CMD ["python", "src.py"]