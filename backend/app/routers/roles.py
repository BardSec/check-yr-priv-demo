import logging

from fastapi import APIRouter, HTTPException, Request

logger = logging.getLogger(__name__)

from app.auth.session import get_session
from app.models.roles import DashboardData
from app.services.analyzer import build_dashboard
from app.services.demo_data import (
    get_active_role_assignments,
    get_ca_policies,
    get_eligible_role_assignments,
    get_organization,
)

router = APIRouter(prefix="/api", tags=["roles"])


@router.get("/dashboard", response_model=DashboardData)
async def dashboard(request: Request):
    session = await get_session(request)
    if not session.get("account"):
        raise HTTPException(status_code=401, detail="Not authenticated")

    org = get_organization()
    active = get_active_role_assignments()
    eligible = get_eligible_role_assignments()
    ca = get_ca_policies()

    return build_dashboard(org, active, eligible, ca)


@router.get("/health")
async def health():
    return {"status": "ok"}
