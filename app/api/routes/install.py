from typing import Any
import datetime

from fastapi import APIRouter, HTTPException

from app.models import Account, Token
from app.api.deps import SessionDep
from app.hubspot.helpers import get_tokens, get_portal_info
from app.database.helpers import create_account, create_token

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
    
    account = Account(
        portal_id=portal_info['hub_id'],
        hub_domain=portal_info['hub_domain'],
        install_user_id=portal_info['user_id'],
        install_date=datetime.datetime.now(),
        install_user_email=state
    )
    created_account = create_account(session=session, account=account)
    account_id = created_account.id

    token = Token(
        account_id=account_id,
        hs_refresh_token=tokens['refresh_token'],
        hs_access_token=tokens['access_token']
    )
    created_token = create_token(session=session, token=token)

