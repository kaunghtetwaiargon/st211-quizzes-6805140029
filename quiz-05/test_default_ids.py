import pytest

@pytest.mark.parametrize("user", [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
], ids=["alice-adult", "bob-adult"]) #one label per each user
def test_user_has_name(user): #pytest generate the ID for each user and ID always starts from "0"
    assert "name" in user