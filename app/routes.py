from fastapi import APIRouter
import time
import random

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/slow")
def slow():
    time.sleep(random.uniform(1, 3))
    return {"message": "Slow response"}

@router.get("/error")
def error():
    if random.random() > 0.5:
        raise Exception("Simulated failure")
    return {"message": "No error"}