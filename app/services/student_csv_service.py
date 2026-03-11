from typing import List, Dict
import csv as csv_module

from app.models.student_model import Student
from app.services.abstract_methods import DataSource


class StudentCSVDataSource(DataSource):
    REQUIRED_FIELDS = ["student", "coffee_spent"]

    def __init__(self, file_paths: List[str]):
        if not file_paths:
            raise FileNotFoundError(
                "Не предоставлено ни одного CSV-файла для обработки"
            )
        self.file_paths = file_paths

    def get_students(self) -> List[Student]:
        students_dict: Dict[str, List[float]] = {}
        for file_path in self.file_paths:
            rows = self._parse_csv(file_path)
            for row in rows:
                student_name = row.get("student", "").strip()
                coffee_spent = row.get("coffee_spent", "").strip()
                if not student_name:
                    continue
                if student_name not in students_dict:
                    students_dict[student_name] = []
                try:
                    coffee_value = float(coffee_spent)
                    students_dict[student_name].append(coffee_value)
                except ValueError:
                    continue
        return [
            Student(name=name, coffee_spent=list(expenses))
            for name, expenses in students_dict.items()
        ]

    @staticmethod
    def _parse_csv(file_path: str) -> List[Dict[str, str]]:
        result = []
        with open(file_path, "r", encoding="utf-8", newline="") as f:
            reader = csv_module.DictReader(f)
            for row in reader:
                result.append(row)
        return result
