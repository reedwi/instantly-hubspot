from sqlmodel import Session

from app.database.helpers import get_account_by_webhook, get_tokens
from app.hubspot.helpers import find_contact

def process_instantly_webhook(webhook_body, session: Session, wh_id: str):
    event_type = webhook_body['event_type']
    account_id = get_account_by_webhook(session=session, webhook_id=wh_id)
    tokens = get_tokens(session=session, account_id=account_id)
    hs_contact_id = find_contact(access_token=tokens.hs_access_token, email=webhook_body['email'])
    

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