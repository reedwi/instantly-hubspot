from app.models import Account, Token
from sqlmodel import Session

def create_account(*, session: Session, account: Account) -> Account:
    db_obj = Account.model_validate(account)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def create_token(*, session: Session, token: Token) -> Account:
    db_obj = Token.model_validate(token)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj