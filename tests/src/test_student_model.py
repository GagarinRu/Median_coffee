from app.models.student_model import Student


def test_student_median_odd_count():
    """Медиана для нечетного количества значений."""
    student = Student(name="Test", coffee_spent=[100, 200, 300])
    assert student.median_coffee == 200


def test_student_median_even_count():
    """Медиана для четного количества значений."""
    student = Student(name="Test", coffee_spent=[100, 200, 300, 400])
    assert student.median_coffee == 250


def test_student_median_single_value():
    """Медиана для одного значения."""
    student = Student(name="Test", coffee_spent=[150])
    assert student.median_coffee == 150


def test_student_median_empty():
    """Медиана для пустого списка."""
    student = Student(name="Test", coffee_spent=[])
    assert student.median_coffee == 0.0


def test_student_median_sorted():
    """Вычисление медианы для несортированного списка."""
    student = Student(name="Test", coffee_spent=[300, 100, 200])
    assert student.median_coffee == 200
