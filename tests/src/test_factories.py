import pytest

from app.services.median_coffee_service import MedianCoffeeReport
from app.utils.factories import ReportFactory, StudentService


def test_report_factory():
    """Проверка разных типов отчета."""
    report = ReportFactory.create("median-coffee")
    assert isinstance(report, MedianCoffeeReport)
    with pytest.raises(ValueError, match="Неизвестный тип отчета"):
        ReportFactory.create("unknown_report")


class MockDataSource:
    def get_students(self):
        return []


def test_student_service():
    """Проверка сервиса студентов."""
    mock_ds = MockDataSource()
    service = StudentService(mock_ds)
    with pytest.raises(ValueError, match="Данные о студентах отсутствуют"):
        service.get_report("median-coffee")
