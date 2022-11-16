from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn


from payment_checkout_api.app.database import crud, models
from payment_checkout_api.app.models import schemas
from payment_checkout_api.app.database.database import SessionLocal, engine
from payment_checkout_api.app.services.webhook import Webhook

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# webhook
# https://fiapcom.webhook.office.com/webhookb2/8cf1d42e-933f-4b80-9131-bb37825418c5@11dbbfe2-89b8-4549-be10-cec364e59551/IncomingWebhook/3981c10a9ad24a1d8fe9d2a40fb5e26d/8bc263ea-bde7-4fd5-bc37-a8c0fb3b34d1

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/payments", response_model=list[schemas.Payment], description='List all payments')
def list_users(db: Session = Depends(get_db)):
    return crud.get_payments(db=db)


@app.post("/payment", response_model=schemas.Payment, description='Create new Payment', status_code=201)
def create_payment(payment: schemas.PaymentCreateConsumer, db: Session = Depends(get_db)):
    input = schemas.PaymentCreate(**payment.dict())
    new_payment = crud.create_payment(
        db=db, payment=input)
    return new_payment


@app.patch("/payment", response_model=schemas.Payment, description='Update payment status')
def update_payment(payment: schemas.PaymentUpdateStatus, db: Session = Depends(get_db)):
    updated_payment = crud.update_payment(
        db=db, payment=payment)
    webhook = Webhook()
    webhook.notify_msteams(payment)
    return updated_payment


@app.delete("/payments", response_model=schemas.Payment, description='Delete payment', )
def delete_payment(payment: schemas.PaymentDelete, db: Session = Depends(get_db)):
    updated_payment = crud.delete_payment(
        db=db, payment=payment)
    return None

# @app.post("/users", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

#     new_user = crud.create_user(db=db, user=user)
#     novas_imagens = [Image]
#     if user.images is not None:
#         for image in user.images:
#             image.base64 = base64.decodebytes(image.base64.encode("ascii"))
#             crud.create_user_image(
#                 db=db, image=ImageCreate2(**image.dict()), user_id=new_user.id
#             )

#     for image in new_user.images:
#         image.base64 = base64.encodebytes(image.base64).decode("ascii")[:-1]
#     # print(base64.encode(new_user.images[0].base64))
#     return new_user


# @app.get("/users", response_model=list[schemas.User])
# def list_users(db: Session = Depends(get_db)):
#     users = crud.get_users(db=db)
#     for user in users:
#         for image in user.images:
#             image.base64 = base64.encodebytes(image.base64).decode("ascii")[:-1]
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def list_users(user_id: int, db: Session = Depends(get_db)):
#     user = crud.get_user(db=db, user_id=user_id)
#     for image in user.images:
#         image.base64 = base64.encodebytes(image.base64).decode("ascii")[:-1]
#     return user


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
