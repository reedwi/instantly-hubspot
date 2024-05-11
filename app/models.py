from typing import Optional
import datetime

from sqlmodel import Field, SQLModel, MetaData
from pydantic import BaseModel

metadata = MetaData(schema="instantly_hubspot")

class Account(SQLModel, table=True):
    metadata = MetaData(schema="instantly_hubspot")
    id: Optional[str] = Field(default=None, primary_key=True)
    portal_id: int
    hub_domain: str
    install_user_email: str
    install_user_id: str
    install_date: datetime.datetime
    created_at: Optional[datetime.datetime]


class Subscription(SQLModel, table=True):
    metadata = MetaData(schema="instantly_hubspot")
    id: Optional[str] = Field(default=None, primary_key=True)
    start_date: datetime.datetime
    end_date: datetime.datetime
    tier: str
    created_at: Optional[datetime.datetime]


class Payment(SQLModel, table=True):
    metadata = MetaData(schema="instantly_hubspot")
    id: Optional[str] = Field(default=None, primary_key=True)
    amount: float
    purchaser_email: str
    portal_id: int
    created_at: Optional[datetime.datetime]


class Usage(SQLModel, table=True):
    metadata = MetaData(schema="instantly_hubspot")
    id: Optional[str] = Field(default=None, primary_key=True)
    account_id: str =  Field(foreign_key="account.id")
    created_at: Optional[datetime.datetime]


class SubscriptionAccount(SQLModel, table=True):
    metadata = MetaData(schema="instantly_hubspot")
    id: Optional[str] = Field(default=None, primary_key=True)
    account_id: str =  Field(foreign_key="account.id")
    subscription_id: str = Field(foreign_key="subscription.id")
    created_at: Optional[datetime.datetime]


class PaymentSubscription(SQLModel, table=True):
    metadata = MetaData(schema="instantly_hubspot")
    id: Optional[str] = Field(default=None, primary_key=True)
    payment_id: str =  Field(foreign_key="payment.id")
    subscription_id: str = Field(foreign_key="subscription.id")
    created_at: Optional[datetime.datetime]


class PaymentAccount(SQLModel, table=True):
    metadata = MetaData(schema="instantly_hubspot")
    id: Optional[str] = Field(default=None, primary_key=True)
    account_id: str =  Field(foreign_key="account.id")
    payment_id: str = Field(foreign_key="payment.id")
    created_at: Optional[datetime.datetime]


class Token(SQLModel, table=True):
    metadata = MetaData(schema="instantly_hubspot")
    id: Optional[str] = Field(default=None, primary_key=True)
    account_id: str =  Field(foreign_key="account.id")
    hs_access_token: Optional[str]
    hs_refresh_token: Optional[str]
    hs_expires_at: Optional[datetime.datetime]
    instantly_key: Optional[str]
    created_at: Optional[datetime.datetime]


class HubspotHook(BaseModel):
    pass