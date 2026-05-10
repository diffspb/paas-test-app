import os

from fastapi import FastAPI

SERVICE_NAME = "paas-test"
APP_VERSION = os.getenv("APP_VERSION", "0.2.1")
ENVIRONMENT = os.getenv("APP_ENV", "local")

app = FastAPI(title="PaaS Test App", version=APP_VERSION)


@app.get("/")
async def root():
    return {
        "service": SERVICE_NAME,
        "message": "PaaS test application is running",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
    }


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": SERVICE_NAME,
        "version": APP_VERSION,
    }


@app.get("/version")
async def version():
    return {
        "service": SERVICE_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
    }
