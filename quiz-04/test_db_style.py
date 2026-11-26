import pytest


class FakeDatabase:
    def __init__(self):
        self.connected = False
        self.data = []

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False


@pytest.fixture
def database():
    db = FakeDatabase()
    db.connect()

    yield db

    db.disconnect()
    assert db.connected is False


def test_database_connected(database):
    assert database.connected is True


def test_database_starts_with_empty_data(database):
    assert database.data == []


def test_database_can_store_data(database):
    database.data.append("test record")
    assert database.data == ["test record"]
