import pytest

from app.models.student_model import Student


@pytest.fixture
def sample_students():
    return [
        Student(name="Ivan Petrov", coffee_spent=[100, 200, 300]),
        Student(name="Alexander Sidorov", coffee_spent=[150, 250]),
    ]


@pytest.fixture(
    params=[
        ([100, 200, 300], 200),
        ([100, 200, 300, 400], 250),
        ([150], 150),
        ([], 0.0),
        ([300, 100, 200], 200),
    ]
)
def median_cases(request):
    coffee_spent, expected = request.param
    student = Student(name="Test", coffee_spent=coffee_spent)
    return student, expected
