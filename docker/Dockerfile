FROM python:latest

WORKDIR /app

COPY ../requirements.txt .
RUN pip install -r requirements.txt
RUN pip install flask prometheus_client

COPY /app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]