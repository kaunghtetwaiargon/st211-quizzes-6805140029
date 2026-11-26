# Lab 5: Parameterized and Data-Driven Testing

**Course:** 192-211 Automated Software Testing  
**University:** Siam University

## Overview

This lab focuses on parameterized and data-driven testing with `pytest`. Instead of writing separate test functions for similar scenarios, parameterization allows multiple sets of inputs and expected outputs to be tested using a single test function.

## Learning Objectives

- Understand parameterized testing.
- Use `pytest.mark.parametrize` to test multiple input values.
- Apply data-driven testing techniques.
- Verify expected results across different test cases.
- Reduce duplicated test code.
- Improve test readability and maintainability.

## Requirements

- Python 3
- pytest

## Installation

Install pytest using:

```bash
python3 -m pip install pytest
```

## Running the Tests

Run all tests:

```bash
python3 -m pytest -v
```

Run the Lab 5 tests:

```bash
python3 -m pytest quiz-05/ -v
```

## Parameterized Testing Example

The following example demonstrates testing multiple input combinations with one test function.

```python
import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (10, 5, 15),
        (-1, 1, 0),
        (0, 0, 0),
    ],
)
def test_add(a, b, expected):
    assert a + b == expected
```

### Explanation

- `@pytest.mark.parametrize` supplies multiple sets of test data.
- `a` and `b` represent the input values.
- `expected` represents the expected result.
- pytest runs the test function once for each data set.

## Benefits of Parameterized Testing

- Reduces duplicated test code.
- Tests multiple scenarios efficiently.
- Makes test cases easier to maintain.
- Improves coverage of different input combinations.
- Makes failures easier to identify for individual test cases.

## Conclusion

Parameterized and data-driven testing help create efficient, reusable, and maintainable automated tests by applying multiple data sets to the same test logic.