import pytest

from app.services.median_coffee_service import MedianCoffeeReport
from app.models.student_model import Student


@pytest.mark.parametrize(
    "students,expected_order",
    [
        (
            [
                Student(name="B", coffee_spent=[100]),
                Student(name="A", coffee_spent=[200]),
                Student(name="C", coffee_spent=[50]),
            ],
            ["A", "B", "C"],
        ),
        (
            [
                Student(name="X", coffee_spent=[500]),
                Student(name="Y", coffee_spent=[100]),
            ],
            ["X", "Y"],
        ),
    ],
)
def test_median_coffee_report_sorted_descending(students, expected_order):
    """Отчет отсортирован по убывающей медиане."""
    report = MedianCoffeeReport()
    result = report.generate(students)
    for i in range(len(expected_order) - 1):
        assert result.index(expected_order[i]) < result.index(expected_order[i + 1])


def test_median_coffee_report_empty():
    """Отчет с пустым списком студентов."""
    report = MedianCoffeeReport()
    result = report.generate([])
    lines = result.split("\n")
    assert len(lines) >= 2


@pytest.mark.parametrize(
    "coffee_spent,expected_median",
    [
        ([100, 200, 300], "200"),
        ([50, 150], "100"),
        ([100], "100"),
    ],
)
def test_median_coffee_report_values(coffee_spent, expected_median):
    """Отчет с различными средними значениями."""
    students = [Student(name="Test", coffee_spent=coffee_spent)]
    report = MedianCoffeeReport()
    result = report.generate(students)
    assert "Test" in result
    assert expected_median in result
