# IAM CaaS Starter (AWS + FastAPI + PingOne)

This is a minimal starter for your IAM Compliance-as-a-Service platform.

## What’s inside
- **FastAPI** backend, deployable to **AWS Lambda** (via `mangum`)
- Basic models for tenants and findings
- PingOne API client (client-credentials flow)
- Simple compliance checks (MFA + stale accounts)
- Minimal React + Tailwind app scaffold

> Note: Values/URLs for PingOne vary by region. Update `.env.example` accordingly.

## Quick start (local)

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env  # set values
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs

## Deploy targets
- API Gateway + Lambda (handler in `app/main.py` via `Mangum`)
- Aurora Serverless v2 (PostgreSQL) — wiring left for Infra-as-code
- EventBridge for scheduled syncs — see `app/services/scheduler_notes.md`

## Frontend
Inside `frontend/` you’ll find a minimal Vite + React scaffold with Tailwind.
