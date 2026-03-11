import json

from app.utils.factories import StudentService


class ReportController:
    """Контроллер версий обработки данных."""

    def __init__(
        self,
        service: StudentService,
    ):
        self.service = service

    def handle_request(self, report_type: str) -> str:
        """Проверка типа отчета."""
        try:
            report_data = self.service.get_report(report_type)
            return report_data
        except Exception as e:
            return json.dumps({"Ошибка": str(e)}, ensure_ascii=False)
