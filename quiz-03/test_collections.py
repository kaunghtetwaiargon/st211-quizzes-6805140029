def test_list_equality():
    assert [1, 2, 3] == [1, 2, 3]


def test_list_contents():
    result = [3, 1, 2]

    assert sorted(result) == [1, 2, 3]


def test_dictionary_equality():
    expected = {"name": "Alice", "age": 30}
    actual = {"age": 30, "name": "Alice"}

    assert actual == expected


def test_set_intersection():
    assert {1, 2, 3} & {2, 3, 4} == {2, 3}


def test_empty_list():
    assert [] == []


def test_list_length():
    items = ["apple", "banana", "orange"]

    assert len(items) == 3


def test_dictionary_value():
    student = {"name": "Alice", "age": 20}

    assert student["name"] == "Alice"


def test_set_membership():
    numbers = {1, 2, 3}

    assert 2 in numbers