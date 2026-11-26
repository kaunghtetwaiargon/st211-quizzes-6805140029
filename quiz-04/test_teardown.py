import pytest


@pytest.fixture
def temp_file(tmp_path):
    filename = tmp_path / "test_data.txt"

    filename.write_text("test content")

    print("\n[setup] file created")

    yield filename

    if filename.exists():
        filename.unlink()

    print("\n[teardown] file removed")


def test_file_exists(temp_file):
    assert temp_file.exists()


def test_file_content(temp_file):
    assert temp_file.read_text() == "test content"


def test_file_can_be_written(temp_file):
    temp_file.write_text("updated content")
    assert temp_file.read_text() == "updated content"
