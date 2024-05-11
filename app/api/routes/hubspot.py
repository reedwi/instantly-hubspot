from typing import Any

from fastapi import APIRouter, HTTPException

from app.models import Account
from app.api.deps import SessionDep

router = APIRouter()


@router.get("/")
def hubspot_hook(session: SessionDep) -> Any:
    pass

