FROM python:3.13-slim
LABEL maintainer="shcherbdmytro@gmail.com"

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
