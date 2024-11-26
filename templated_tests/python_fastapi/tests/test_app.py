import pytest
from fastapi.testclient import TestClient
from myapp.app import app
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
    response = client.get("/sqrt/9")
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}


def test_echo():
    response = client.get("/echo/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "hello"}


def test_days_until_new_year():
    response = client.get("/days-until-new-year")
    assert response.status_code == 200
    today = date.today()
    next_new_year = date(today.year + 1, 1, 1)
    delta = next_new_year - today
    assert response.json() == {"days_until_new_year": delta.days}


def test_is_palindrome():
    response = client.get("/is-palindrome/racecar")
    assert response.status_code == 200
    assert response.json() == {"is_palindrome": True}


def test_square():
    response = client.get("/square/4")
    assert response.status_code == 200
    assert response.json() == {"result": 16}


def test_division():
    response = client.get("/divide/10/2")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_multiplication():
    response = client.get("/multiply/3/5")
    assert response.status_code == 200
    assert response.json() == {"result": 15}


def test_subtraction():
    response = client.get("/subtract/10/4")
    assert response.status_code == 200
    assert response.json() == {"result": 6}


def test_sqrt_negative_number():
    response = client.get("/sqrt/-4")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot take square root of a negative number"}


def test_divide_by_zero():
    response = client.get("/divide/10/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}


def test_addition():
    response = client.get("/add/3/5")
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_current_date():
    response = client.get("/current-date")
    assert response.status_code == 200
    assert response.json() == {"date": date.today().isoformat()}

