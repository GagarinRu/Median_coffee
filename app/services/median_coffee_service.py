from typing import List

from tabulate import tabulate

from app.models.student_model import Student


class MedianCoffeeReport:
    def generate(self, data: List[Student]) -> str:
        sorted_students = sorted(data, key=lambda s: s.median_coffee, reverse=True)
        table_data = [
            [student.name, student.median_coffee] for student in sorted_students
        ]
        headers = ["Студент", "Медиана трат на кофе"]
        return tabulate(table_data, headers=headers, tablefmt="grid")
