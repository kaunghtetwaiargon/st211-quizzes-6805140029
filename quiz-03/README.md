# Lab 3: Assertions and Test Organization

## Course

192-211 Automated Software Testing

## Objectives

- Practice different assertion types.
- Test collections and floating-point numbers.
- Organize related tests into classes.
- Use pytest markers.
- Skip tests when necessary.
- Mark known failures with xfail.
- Configure pytest with pytest.ini.

## Project Structure

- assertions_demo.py: Functions for assertion examples.
- test_assertions.py: Basic assertions.
- test_collections.py: List, dictionary, and set assertions.
- test_floats.py: Floating-point assertions.
- shopping.py: ShoppingCart implementation.
- test_shopping.py: ShoppingCart test class.
- test_markers.py: Smoke, slow, and regression tests.
- test_skips.py: Skip and skipif examples.
- test_xfail.py: Expected failure example.
- test_conditional.py: Conditional skip example.
- pytest.ini: Pytest configuration.

## Setup

Install pytest:

    python3 -m pip install pytest

## Run All Tests

From this directory:

    python3 -m pytest

## Run Selected Tests

Run smoke tests:

    python3 -m pytest -m smoke

Run regression tests:

    python3 -m pytest -m regression

Exclude slow tests:

    python3 -m pytest -m "not slow"

Run collection tests:

    python3 -m pytest test_collections.py

Run the ShoppingCart test class:

    python3 -m pytest test_shopping.py::TestShoppingCart

## Expected Results

- Normal tests should pass.
- The explicitly skipped test should be reported as SKIPPED.
- The known-broken test should be reported as XFAIL.
- Unexpected failures should be investigated rather than hidden.