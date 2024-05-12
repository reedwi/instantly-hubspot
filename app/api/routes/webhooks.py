from typing import Any

from fastapi import APIRouter, HTTPException

from app.models import Account, InstantlyHook
from app.api.deps import SessionDep
from app.database.helpers import create_instantly_hook
from app.core.config import settings

router = APIRouter()


@router.get("/{id}", response_model=Account)
async def trigger_webhook(session: SessionDep, id: str) -> Any:
    #TODO: all the stuff that needs to happen when instantly hook triggers
    pass


@router.post("/", response_model=InstantlyHook)
def create_webhook(*, session: SessionDep, code: str) -> Any:
    #TODO: Determine what we get from account setup page in HS to find account
    account = session.get(Account, id)
    hook = InstantlyHook(
        account_id=account.id
    )
    created_hook = create_instantly_hook(hook)
    domain = f'{settings.WEBHOOK_URL}/{created_hook.id}'
    return domain
