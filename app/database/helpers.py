from app.models import Account, Token, InstantlyHook, Payment
from sqlmodel import Session, select

def create_account(*, session: Session, account: Account) -> Account:
    db_obj = Account.model_validate(account)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def create_token(*, session: Session, token: Token) -> Token:
    db_obj = Token.model_validate(token)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

# def get_account(*, session: Session, account: Token) -> Account:
#     db_obj = Account.model_validate(account)
#     session.add(db_obj)
#     session.commit()
#     session.refresh(db_obj)
#     return db_obj

def create_instantly_hook(*, session: Session, hook: InstantlyHook) -> InstantlyHook:
    db_obj: InstantlyHook = InstantlyHook.model_validate(hook)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def create_payment(*, session: Session, payment: Payment) -> Payment:
    db_obj = Payment.model_validate(payment)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_payment_by_checkout(session: Session, checkout_id: str) -> Payment:
    db_obj = session.exec(
        select(Payment).where(Payment.stripe_checkout_id == checkout_id)
    ).first()
    return db_obj