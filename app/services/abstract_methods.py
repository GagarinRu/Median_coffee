from typing import Protocol, List

from app.models.student_model import Student


class DataSource(Protocol):
    def get_students(self) -> List[Student]: ...


class Report(Protocol):
    def generate(self, data: List[Student]) -> str: ...
