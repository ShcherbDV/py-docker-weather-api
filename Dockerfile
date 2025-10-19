FROM python:3.13-slim
LABEL maintainer="shcherbdmytro@gmail.com"

ENV PYTHOUNNBUFFERED=1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "runserver", "0.0.0.0:8000"]
