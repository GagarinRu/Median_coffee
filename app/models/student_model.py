import statistics
from dataclasses import dataclass, field


@dataclass
class Student:
    """Модель студента."""

    name: str
    coffee_spent: list[float] = field(default_factory=list)

    @property
    def median_coffee(self) -> float:
        if not self.coffee_spent:
            return 0.0
        try:
            return statistics.median(self.coffee_spent)
        except statistics.StatisticsError:
            return 0.0
