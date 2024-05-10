from typing import Any

from fastapi import APIRouter, HTTPException

from app.models import Account
from app.api.deps import SessionDep
from app.hubspot.helpers import get_tokens, get_portal_info

router = APIRouter()


@router.get("/", response_model=Account)
def get_install(session: SessionDep, code: str, state: str) -> Any:
    tokens = get_tokens(
        code=code,
        grant_type='authorization_code'
    )
    if not tokens:
        raise HTTPException(status_code=404, detail="Error getting access tokens")

    portal_info = get_portal_info(tokens['access_token'])
    if not portal_info:
        raise HTTPException(status_code=404, detail="Error getting portal info")
    
    #TODO: Finish install flow, create an account
