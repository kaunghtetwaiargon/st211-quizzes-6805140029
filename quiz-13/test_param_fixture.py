import pytest

@pytest.fixture(params=["sqlite", "postgres", "mysql"])
def database_type(request):
    # request is a special built-in pytest object
    return request.param

def test_database_connection(database_type):
    print(f"\nTesting with {database_type}")
    assert database_type in ["sqlite", "postgres", "mysql"]
