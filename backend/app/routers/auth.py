"""
Demo auth router — skips Microsoft OAuth entirely.
Clicking "Sign in" immediately creates an authenticated session
with a realistic demo user, so the app looks production-like for
screenshots, documentation, and demo videos.
"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, RedirectResponse

from app.auth.session import clear_session, get_session, save_session
from app.config import settings

# Realistic demo user — matches the Contoso tenant in demo_data.py
_DEMO_USER = {
    "oid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "name": "Alice Chen",
    "preferred_username": "alice.chen@contoso.com",
    "tid": "4a7f3b21-e89c-4d56-b12a-8f90c4d5e6a7",
}

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/login")
async def login(request: Request):
    """Demo login — no OAuth redirect, immediately sets a session."""
    response = RedirectResponse(settings.app_base_url)
    await save_session(response, {"account": _DEMO_USER})
    return response


@router.get("/me")
async def me(request: Request):
    session = await get_session(request)
    account = session.get("account")
    if not account:
        return JSONResponse({"authenticated": False}, status_code=401)
    return {"authenticated": True, "user": account}


@router.post("/logout")
async def logout(request: Request):
    response = RedirectResponse(settings.app_base_url)
    await clear_session(request, response)
    return response
