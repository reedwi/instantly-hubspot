from typing import Any

from fastapi import APIRouter, HTTPException, Request

from app.models import Payment
from app.api.deps import SessionDep
from app.database.helpers import create_payment

router = APIRouter()



@router.post("/")
async def create_payment_api(request: Request, session: SessionDep, code: str) -> Any:
    stripe_hook = request.body()
    payment = Payment(
        amount=stripe_hook['object']['amount_total'],
        purchaser_email=stripe_hook['customer_details']['email'],
        stripe_checkout_id=stripe_hook['object']['id'],
        portal_id=stripe_hook['custom_fields'][0]['numeric']['value']
    )
    created_payment = create_payment(session=session, payment=payment)
    return
