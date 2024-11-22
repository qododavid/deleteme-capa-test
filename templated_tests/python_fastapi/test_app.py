import pytest
from fastapi.testclient import TestClient
from app import app
from datetime import date

client = TestClient(app)

def test_root():
    """
    Test the root endpoint by sending a GET request to "/" and checking the response status code and JSON body.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application!"}


def test_sqrt_positive_number():
    response = client.get("/sqrt/4")
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}


def test_echo_message():
    response = client.get("/echo/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "hello"}


def test_days_until_new_year():
    response = client.get("/days-until-new-year")
    assert response.status_code == 200
    # Calculate expected days until new year
    today = date.today()
    next_new_year = date(today.year + 1, 1, 1)
    expected_days = (next_new_year - today).days
    assert response.json() == {"days_until_new_year": expected_days}


def test_is_palindrome():
    response = client.get("/is-palindrome/racecar")
    assert response.status_code == 200
    assert response.json() == {"is_palindrome": True}


def test_square_number():
    response = client.get("/square/3")
    assert response.status_code == 200
    assert response.json() == {"result": 9}


def test_divide_non_zero():
    response = client.get("/divide/10/2")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_multiply_positive_integers():
    response = client.get("/multiply/4/5")
    assert response.status_code == 200
    assert response.json() == {"result": 20}


def test_subtract_positive_integers():
    response = client.get("/subtract/10/3")
    assert response.status_code == 200
    assert response.json() == {"result": 7}


def test_sqrt_negative_number():
    response = client.get("/sqrt/-4")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot take square root of a negative number"}


def test_divide_by_zero():
    response = client.get("/divide/10/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}


def test_add_positive_integers():
    response = client.get("/add/3/5")
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_current_date():
    response = client.get("/current-date")
    assert response.status_code == 200
    assert response.json() == {"date": date.today().isoformat()}

