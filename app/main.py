import json
import sys

from app.core.argparse import setup_client
from app.services.student_csv_service import StudentCSVDataSource
from app.services.report_service import ReportController
from app.utils.factories import StudentService


def main():
    """Основная функция обработки данных о студентах."""
    try:
        args = setup_client()
        csv_files = args.files
        if not csv_files:
            print(
                "Ошибка: не указаны файлы для обработки. Используйте --files",
                file=sys.stderr,
            )
            sys.exit(1)
        data_source = StudentCSVDataSource(csv_files)
        service = StudentService(data_source)
        controller = ReportController(service)
        result = controller.handle_request(args.report)
        print(result)
    except FileNotFoundError as e:
        print(json.dumps({"Ошибка": str(e)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"Ошибка": str(e)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
