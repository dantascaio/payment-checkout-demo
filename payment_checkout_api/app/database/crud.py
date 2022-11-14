from sqlalchemy.orm import Session

from ..models import schemas

from . import models


def get_payment(db: Session, payment_id: int):
    return db.query(models.Payment).filter(models.Payment.payment_id == payment_id).first()


def get_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Payment).offset(skip).limit(limit).all()


def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = models.Payment(
        payer_name=payment.payer_name,
        card_number=payment.card_number,
        payment_value=payment.payment_value,
        status_code=payment.status_code,
        status=payment.status,
        authorization_timestamp=payment.authorization_timestamp,
        zip_code=payment.zip_code
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


def update_payment(db: Session, payment: schemas.PaymentUpdateStatus):
    obj = db.query(models.Payment).filter(
        models.Payment.payment_id == payment.payment_id).first()
    obj.status_code = payment.new_status_code
    db.commit()
    db.refresh(obj)
    return obj


def delete_payment(db: Session, payment: schemas.PaymentUpdateStatus):
    obj = db.query(models.Payment).filter(
        models.Payment.payment_id == payment.payment_id).first()
    if obj is not None:
        db.delete(obj)
        db.commit()
    else:
        pass

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()

# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()

# def create_user(db: Session, user: schemas.UserCreate):
#     db_user = models.User(name=user.name)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def create_payment(db: Session, payment: schemas.PaymentCreate):
#     db_user = models.Payment(name=payment.name)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_image(db: Session, image: schemas.ImageCreate2, user_id: int):
#     db_image = models.Image(**image.dict(), user_id=user_id)
#     db.add(db_image)
#     db.commit()
#     db.refresh(db_image)
#     return db_image
