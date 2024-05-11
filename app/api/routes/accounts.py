from typing import Any

from fastapi import APIRouter, HTTPException

from app.models import Account
from app.api.deps import SessionDep

router = APIRouter()


@router.get("/{id}", response_model=Account)
def get_account(session: SessionDep, id: str) -> Any:
    account = session.get(Account, id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account


@router.post("/", response_model=Account)
def create_account(*, session: SessionDep, item_in: Account) -> Any:
    account = Account.model_validate(item_in)
    session.add(account)
    session.commit()
    session.refresh(account)
    return account
