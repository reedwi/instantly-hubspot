from typing import Any

from fastapi import APIRouter, HTTPException

from app.models import Account, InstantlyHook
from app.api.deps import SessionDep
from app.database.helpers import create_instantly_hook
from app.core.config import settings

router = APIRouter()

