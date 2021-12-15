from dataclasses import dataclass

import pytest
from fastapi.testclient import TestClient

from app.main import app


@dataclass
class TestData:
    req = {}
    emp_count = 0


@pytest.fixture(scope='session')
def response_data():
    data = TestData()
    return data


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="module")
def test_data():
    test_employee_data = \
        {
            "name": "Alex Martin",
            "email": "example@google.com",
            "age": 33,
            "company": "ExampleCompany",
            "join_date": "2002-12-25T05:04:16-08:00",
            "job_title": "driver",
            "gender": "male",
            "salary": 1250
        }
    return test_employee_data
