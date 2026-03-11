import argparse
from app.utils.factories import ReportFactory


def setup_client() -> argparse.Namespace:
    """Настройка argparse."""
    parser = argparse.ArgumentParser(
        description="Анализ данных о подготовке студентов к экзаменам"
    )
    parser.add_argument(
        "--files", nargs="+", default=[], help="CSV файлы для обработки"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=ReportFactory.get_available_reports(),
        help=f"Тип отчёта ({', '.join(ReportFactory.get_available_reports())})",
    )
    return parser.parse_args()
