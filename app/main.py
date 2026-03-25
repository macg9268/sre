from fastapi import FastAPI, Request, Response, HTTPException
import time
import asyncio
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()

# =========================
# 📊 METRICS
# =========================

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency",
    ["endpoint"]
)

ERROR_COUNT = Counter(
    "http_errors_total",
    "Total HTTP errors",
    ["endpoint", "status"]
)

# =========================
# ⚙️ MIDDLEWARE
# =========================

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    if request.url.path == "/metrics":
        return await call_next(request)

    start_time = time.time()

    try:
        response = await call_next(request)
        status_code = response.status_code
    except Exception:
        status_code = 500
        ERROR_COUNT.labels(request.url.path, status_code).inc()
        raise
    finally:
        latency = time.time() - start_time

        REQUEST_COUNT.labels(
            request.method,
            request.url.path,
            str(status_code)  # 👈 ensure string
        ).inc()

        REQUEST_LATENCY.labels(
            request.url.path
        ).observe(latency)

        if status_code >= 400:
            ERROR_COUNT.labels(
                request.url.path,
                str(status_code)
            ).inc()

    return response

# =========================
# 🌐 ENDPOINTS
# =========================

@app.get("/")
async def home():
    return {"message": "OK"}

@app.get("/slow")
async def slow():
    await asyncio.sleep(2)  # ✅ non-blocking
    return {"message": "slow response"}

@app.get("/error")
async def error():
    raise HTTPException(status_code=500, detail="something went wrong")  # ✅ correct

@app.get("/health")
async def health():
    return {"status": "healthy"}

# =========================
# 📡 METRICS
# =========================

@app.get("/metrics")
async def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )