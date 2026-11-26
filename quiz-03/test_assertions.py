from assertions_demo import (
    add,
    is_positive,
    find_name,
    get_value,
)


def test_equality():
    assert add(2, 2) == 4


def test_inequality():
    assert 5 != 3


def test_greater_than():
    assert 10 > 5


def test_less_than_or_equal():
    assert 3 <= 3


def test_boolean_true():
    assert is_positive(5) is True


def test_boolean_false():
    assert is_positive(-2) is False


def test_none():
    assert get_value({}, "missing") is None


def test_string_membership():
    assert "a" in "apple"


def test_list_membership():
    assert 2 in [1, 2, 3]


def test_dictionary_key_membership():
    assert "key" in {"key": "value"}


def test_find_existing_name():
    assert find_name(["Alice", "Bob"], "Alice") is True


def test_find_missing_name():
    assert find_name(["Alice", "Bob"], "Charlie") is False