FROM python:latest

WORKDIR /app

COPY ../requirements.txt .
COPY /app /app/app

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]