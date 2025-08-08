from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.ping_client import PingClient
from ..services.compliance import compute_findings

router = APIRouter()

class PingConnect(BaseModel):
    base_url: str
    environment_id: str
    client_id: str
    client_secret: str

@router.post("/connect")
async def connect_ping(cfg: PingConnect):
    # Simple connectivity check: list users (no persistence in this starter)
    client = PingClient(cfg.base_url, cfg.environment_id, cfg.client_id, cfg.client_secret)
    users = await client.list_users(limit=5)
    return {"connected": True, "sample_users_count": len(users.get("_embedded", {}).get("users", []))}

@router.post("/sync-preview")
async def sync_preview(cfg: PingConnect):
    client = PingClient(cfg.base_url, cfg.environment_id, cfg.client_id, cfg.client_secret)
    # Tiny sample to preview findings
    users = await client.list_users(limit=50)
    activities = {}  # left as an exercise to fetch if your env supports it
    findings = compute_findings(users, activities)
    return {"findings": findings[:20], "total": len(findings)}
