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


def get_account_by_webhook(session: Session, webhook_id: str) -> str:
    db_obj = session.get(InstantlyHook, webhook_id)
    return db_obj.account_id


def get_tokens(session: Session, account_id: str) -> Token:
    db_obj = session.exec(
        select(Token).where(Token.account_id == account_id)
    ).first()
    return db_obj