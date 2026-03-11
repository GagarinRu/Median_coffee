import pytest
import json

from app.services.report_service import ReportController


class MockService:
    """Имитация создания Student."""

    def __init__(self, return_value=None, side_effect=None):
        self.return_value = return_value
        self.side_effect = side_effect

    def get_report(self, report_type):
        if self.side_effect:
            raise self.side_effect
        return self.return_value


def test_report_controller_success():
    """Проверка ReportController на работоспособность."""
    mock_service = MockService(return_value="Test report")
    controller = ReportController(mock_service)
    result = controller.handle_request("median-coffee")
    assert result == "Test report"


def test_report_controller_error_handling():
    """Проверка ReportController проверку ошибок."""
    error_msg = "Test error message"
    mock_service = MockService(side_effect=Exception(error_msg))
    controller = ReportController(mock_service)
    result = controller.handle_request("median-coffee")
    assert "Ошибка" in result
    assert error_msg in result
    try:
        data = json.loads(result)
        assert "Ошибка" in data
    except json.JSONDecodeError:
        pytest.fail("Ответ получен не в формате json")
