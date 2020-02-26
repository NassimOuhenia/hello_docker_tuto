FROM python:3.8.1-slim
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
EXPOSE 80
ENV NOM Docker
CMD ["python", "app/app.py"]
