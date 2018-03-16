FROM python:3.6-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends libssl-dev gcc libc-dev libxml2 bash

COPY requirements.txt /src/

WORKDIR /src

RUN pip3 install -r requirements.txt

COPY ./backup /src

ENTRYPOINT ["python3", "-u", "main.py"]
