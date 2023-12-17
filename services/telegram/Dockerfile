FROM python:3.10.13-bookworm

WORKDIR /usr/src/app/telegram

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat-traditional

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/telegram/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/telegram

RUN chmod +x /usr/src/app/telegram/entrypoint.sh

ENTRYPOINT ["sh", "/usr/src/app/telegram/entrypoint.sh"]