from typing import Any

from fastapi import APIRouter, HTTPException, Request

from app.models import Account, InstantlyHook
from app.api.deps import SessionDep
from app.database.helpers import create_instantly_hook
from app.core.config import settings

router = APIRouter()


@router.post("/{id}")
async def trigger_webhook(request: Request, session: SessionDep, id: str) -> Any:
    #TODO: all the stuff that needs to happen when instantly hook triggers
    body = request.body()
    event_type = body['event_type']
    match event_type:
        case 'lead_interested':
            pass
        case 'email_sent':
            pass
        case 'lead_meeting_booked':
            pass
        case 'lead_meeting_completed':
            pass
        case 'lead_out_of_office':
            pass
        case 'lead_wrong_person':
            pass
        case 'lead_not_interested':
            pass
        case 'campaign_completed':
            pass
        case 'lead_closed':
            pass
        case 'email_opened':
            pass   
        case 'link_clicked':
            pass
        case 'lead_unsubscribed':
            pass  
        case 'reply_received':
            pass  
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
