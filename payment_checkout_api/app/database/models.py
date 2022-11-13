from sqlalchemy import Column, Integer, String, TIMESTAMP

from .database import Base


class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    payer_name = Column(
        String(100),
        # unique=True,
    )
    card_number = Column(String(16))
    payment_value = Column(Integer)
    status_code = Column(Integer)
    status = Column(
        String(30)
    )
    authorization_timestamp = Column(TIMESTAMP)
    zip_code = Column(String(10))
