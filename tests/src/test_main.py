import argparse
import pytest


def test_main_success(monkeypatch, tmp_path, capsys):
    """Успешное выполнение с допустимыми файлами."""
    csv = tmp_path / "students.csv"
    csv.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Ivan Ivanov,2024-06-01,100,7.0,5,good,Math\n"
        "Ivan Ivanov,2024-06-02,200,6.5,6,good,Math\n"
        "Petr Petrov,2024-06-01,150,8.0,3,great,Math\n"
    )
    mock_args = argparse.Namespace(files=[str(csv)], report="median-coffee")
    with monkeypatch.context() as m:
        m.setattr("app.main.setup_client", lambda: mock_args)
        from app.main import main

        main()

    captured = capsys.readouterr()
    assert "Ivan Ivanov" in captured.out
    assert "Petr Petrov" in captured.out


def test_main_no_files_error(monkeypatch, capsys):
    """Ошибка при отсутствии предоставленных файлов."""
    mock_args = argparse.Namespace(files=[], report="median-coffee")
    with monkeypatch.context() as m:
        m.setattr("app.main.setup_client", lambda: mock_args)
        from app.main import main

        with pytest.raises(SystemExit):
            main()
    captured = capsys.readouterr()
    assert "Ошибка" in captured.err or "files" in captured.err.lower()


def test_main_invalid_report(monkeypatch, tmp_path, capsys):
    """Ошибка с неверным типом отчета."""
    csv = tmp_path / "students.csv"
    csv.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Ivan Ivanov,2024-06-01,100,7.0,5,good,Math\n"
    )
    mock_args = argparse.Namespace(files=[str(csv)], report="invalid-report")
    with monkeypatch.context() as m:
        m.setattr("app.main.setup_client", lambda: mock_args)
        from app.main import main

        main()
    captured = capsys.readouterr()
    assert "Ошибка" in captured.out
