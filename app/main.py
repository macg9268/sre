from fastapi import FastAPI
from app.routes import router
from flask import Flask, request

import time
from prometheus_client import Counter, Histogram, generate_latest

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "SRE Reliable API running"}

app = Flask(__name__)

# Metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint', 'status']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'Request latency',
    ['endpoint']
)

@app.route("/")
def home():
    start = time.time()

    status = "200"
    response = "OK"

    REQUEST_COUNT.labels("GET", "/", status).inc()
    REQUEST_LATENCY.labels("/").observe(time.time() - start)

    return response

@app.route("/metrics")
def metrics():
    return generate_latest()