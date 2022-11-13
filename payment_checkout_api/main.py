from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn


from app.database import crud, models
from app.models import schemas
from app.database.database import SessionLocal, engine

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


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/payments", response_model=list[schemas.Payment])
def list_users(db: Session = Depends(get_db)):
    return crud.get_payments(db=db)


@app.post("/payments", response_model=schemas.Payment)
def create_payment(payment: schemas.PaymentCreateConsumer, db: Session = Depends(get_db)):
    input = schemas.PaymentCreate(
        card_number=payment.card_number, payer_name=payment.payer_name, payment_value=payment.payment_value, zip_code=payment.zip_code)
    new_payment = crud.create_payment(
        db=db, payment=input)
    print(f'Tipo do timestamp: {type(new_payment.authorization_timestamp)}')
    return new_payment


@app.patch("/payments", response_model=schemas.Payment)
def create_payment(payment: schemas.PaymentUpdateStatus, db: Session = Depends(get_db)):
    updated_payment = crud.update_payment(
        db=db, payment=payment)
    return updated_payment

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
