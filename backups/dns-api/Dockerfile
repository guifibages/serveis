FROM python:2.7-slim

COPY bind-api.py bind-api.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "bind-api.py"]
