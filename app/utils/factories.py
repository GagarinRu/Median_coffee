from app.services.abstract_methods import Report, DataSource
from app.services.median_coffee_service import MedianCoffeeReport


class ReportFactory:
    """Фабрика отчётов."""

    _reports = {"median-coffee": MedianCoffeeReport}

    @classmethod
    def create(cls, report_type: str) -> Report:
        if report_type not in cls._reports:
            raise ValueError(f"Неизвестный тип отчета: {report_type}")
        return cls._reports[report_type]()

    @classmethod
    def get_available_reports(cls) -> list[str]:
        return list(cls._reports.keys())


class StudentService:
    """Сервисный слой для контроля команд."""

    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def get_report(self, report_type: str) -> str:
        """Проверяем на соответсвие типу данных."""
        students = self.data_source.get_students()
        if not students:
            raise ValueError("Данные о студентах отсутствуют")
        report = ReportFactory.create(report_type)
        return report.generate(students)
