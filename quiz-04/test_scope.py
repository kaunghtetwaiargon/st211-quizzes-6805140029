import pytest


@pytest.fixture(scope="function")
def function_fixture():
    print("\n[function fixture] running")
    return {"scope": "function"}


@pytest.fixture(scope="module")
def module_fixture():
    print("\n[module fixture] running")
    return {"scope": "module"}


def test_one(function_fixture, module_fixture):
    assert function_fixture["scope"] == "function"
    assert module_fixture["scope"] == "module"


def test_two(function_fixture, module_fixture):
    assert function_fixture["scope"] == "function"
    assert module_fixture["scope"] == "module"


def test_three(function_fixture, module_fixture):
    assert function_fixture["scope"] == "function"
    assert module_fixture["scope"] == "module"
