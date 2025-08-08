from fastapi import FastAPI
from mangum import Mangum

from .routers import ping, tenants

app = FastAPI(title="IAM CaaS Starter", version="0.1.0")

@app.get("/health")
def health():
    return {"ok": True}

app.include_router(tenants.router, prefix="/tenants", tags=["tenants"])
app.include_router(ping.router, prefix="/ping", tags=["ping"])

# AWS Lambda handler
handler = Mangum(app)
