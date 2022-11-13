
import datetime
from pydantic import BaseModel, Field


class PaymentBase(BaseModel):
    payer_name: str
    card_number: str = Field(None, max_length=16)
    payment_value: int
    zip_code: str


class PaymentUpdateStatus(BaseModel):
    payment_id: int
    new_status_code: int


class PaymentCreateConsumer(PaymentBase):
    pass


class PaymentCreate(PaymentCreateConsumer):
    status_code: int = 1
    status: str = 'Created'
    authorization_timestamp: datetime.datetime = datetime.datetime.now()


class Payment(PaymentBase):
    status_code: int
    status: str = 'Created'
    payment_id: int
    authorization_timestamp: datetime.datetime

    class Config:
        orm_mode = True


# class ImageBase(BaseModel):
#     base64: str


# class ImageCreate(ImageBase):
#     pass


# class ImageCreate2(BaseModel):
#     base64: bytes


# class Image(ImageBase):
#     id: int
#     user_id: int

#     class Config:
#         orm_mode = True

# payment_id = Column(Integer, primary_key=True, index=True)
# payer_name = Column(
#     String(100),
#     # unique=True,
#     index=True,
# )
# card_number = Column(Integer)
# payment_value = Column(Integer)
# status_code = Column(Integer)
# status = Column(
#     String(30)
# )
# authorization_timestamp = Column(TIMESTAMP)

# class UserBase(BaseModel):
#     name: str


# class UserCreate(UserBase):
#     images: list[ImageCreate] = []


# class User(UserBase):
#     id: int
#     images: list[Image] = []

#     class Config:
#         orm_mode = True
