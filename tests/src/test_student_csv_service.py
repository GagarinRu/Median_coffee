import pytest

from app.services.student_csv_service import StudentCSVDataSource


def test_student_csv_data_source(tmp_path):
    """Чтение CSV-файла с данными студентов."""
    csv = tmp_path / "students.csv"
    csv.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Ivan Ivanov,2024-06-01,100,7.0,5,good,Math\n"
        "Ivan Ivanov,2024-06-02,150,6.5,6,good,Math\n"
        "Petr Petrov,2024-06-01,200,8.0,3,great,Math\n"
    )
    data_source = StudentCSVDataSource([str(csv)])
    students = data_source.get_students()
    assert len(students) == 2
    ivan = next(s for s in students if s.name == "Ivan Ivanov")
    assert ivan.coffee_spent == [100.0, 150.0]
    petr = next(s for s in students if s.name == "Petr Petrov")
    assert petr.coffee_spent == [200.0]


def test_student_csv_multiple_files(tmp_path):
    """Объединение данных из нескольких CSV-файлов."""
    csv1 = tmp_path / "students1.csv"
    csv1.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Ivan Ivanov,2024-06-01,100,7.0,5,good,Math\n"
    )
    csv2 = tmp_path / "students2.csv"
    csv2.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Ivan Ivanov,2024-06-02,150,6.5,6,good,Math\n"
    )
    data_source = StudentCSVDataSource([str(csv1), str(csv2)])
    students = data_source.get_students()
    assert len(students) == 1
    assert students[0].coffee_spent == [100.0, 150.0]


def test_student_csv_empty_file(tmp_path):
    """Обработка пустого CSV-файла."""
    csv = tmp_path / "empty.csv"
    csv.write_text("")
    data_source = StudentCSVDataSource([str(csv)])
    students = data_source.get_students()
    assert len(students) == 0


def test_student_csv_no_files():
    """Ошибка при отсутствии предоставленных файлов."""
    with pytest.raises(FileNotFoundError):
        StudentCSVDataSource([])
