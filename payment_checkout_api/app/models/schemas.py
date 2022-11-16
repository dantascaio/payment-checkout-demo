
import datetime
from enum import Enum
from pydantic import BaseModel, Field


class Status(int, Enum):
    Created = 1
    Processing = 2
    Finished = 3


class PaymentBase(BaseModel):
    payer_name: str
    card_number: str = Field(None, max_length=16)
    payment_value: int
    zip_code: str


class PaymentUpdateStatus(BaseModel):
    payment_id: int
    new_status_code: Status


class PaymentCreateConsumer(PaymentBase):
    pass


class PaymentCreate(PaymentCreateConsumer):
    status_code: Status = 1
    status: str = Status(status_code).name
    authorization_timestamp: datetime.datetime = datetime.datetime.now()


class PaymentDelete(BaseModel):
    payment_id: int


class Payment(PaymentBase):
    status_code: Status
    status: str = 'Created'
    payment_id: int
    authorization_timestamp: datetime.datetime

    class Config:
        orm_mode = True
