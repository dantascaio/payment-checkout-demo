
import datetime
from payment_checkout_api.app.database.database import Base
from payment_checkout_api.app.models import schemas
from payment_checkout_api.app.models.schemas import PaymentCreate, Payment, PaymentUpdateStatus
from payment_checkout_api.main import create_payment, app, get_db, list_users, update_payment
# from payment_checkout_api.app.services.payment import list_users
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

# payment = Payment(**{
#     'payer_name': 'test user',
#     'card_number':  "1234567890123456",
#     'payment_value': 1000,
#     'zip_code': '21345',
#     'status_code': 1,
#     'payment_id': 1,
#     'authorization_timestamp': datetime.datetime.now()
# })


# @pytest.fixture
# def mock_save_analysis_in_db(mocker: MockerFixture):
#     mocker.patch('payment_checkout_api.app.database.crud.create_payment',
#                  return_value=payment)


def test_list_users():
    db = next(override_get_db())
    assert isinstance(list_users(db), list)


def test_create_payment():
    samples = {
        'payer_name': 'test user',
        'card_number':  "1234567890123456",
        'payment_value': 1000,
        'zip_code': '21345',
    }
    request = PaymentCreate(**samples)
    response = create_payment(payment=request, db=next(override_get_db()))
    assert response.status == "Created"
    assert response.status_code == 1


def test_update_payment():
    samples = {
        'payer_name': 'test user',
        'card_number':  "1234567890123456",
        'payment_value': 1000,
        'zip_code': '21345',
    }
    request = PaymentCreate(**samples)
    response = create_payment(payment=request, db=next(override_get_db()))
    payment_to_update = PaymentUpdateStatus(
        payment_id=response.payment_id, new_status_code=2)
    response = update_payment(
        payment=payment_to_update, db=next(override_get_db()))
    assert response.status == "Processing"
    assert response.status_code == 2
