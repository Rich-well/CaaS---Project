from fastapi import APIRouter
from uuid import uuid4

router = APIRouter()

# In-memory store for demo purposes (replace with Postgres)
TENANTS = {}

@router.post("")
def create_tenant(name: str, contact_email: str | None = None):
    tid = str(uuid4())
    TENANTS[tid] = {"id": tid, "name": name, "contact_email": contact_email}
    return TENANTS[tid]

@router.get("")
def list_tenants():
    return list(TENANTS.values())
