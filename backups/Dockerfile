FROM python:3.6-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends libssl-dev gcc libc-dev libxml2

COPY requirements.txt /src/

WORKDIR /src

RUN pip3 install -r requirements.txt

RUN mkdir -p /backup

COPY . /src

ENTRYPOINT ["python", "list.py"]
