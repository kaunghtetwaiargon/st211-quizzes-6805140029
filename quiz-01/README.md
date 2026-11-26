# Lab 1: Testing Fundamentals and Your First Automated Test

**Course:** 192-211 Automated Software Testing  
**University:** Siam University

## Overview

This lab introduces the fundamentals of automated software testing using Python and pytest. It covers writing test functions, using assertions, running automated tests, understanding test results, and testing real functions.

## Learning Objectives

- Install and run pytest.
- Write automated test functions.
- Use assertions to verify expected results.
- Understand passing and failing tests.
- Apply the Arrange, Act, Assert (AAA) pattern.
- Test functions that raise exceptions.
- Run individual tests and the entire test suite.

## Lab Contents

| File | Description |
|---|---|
| `test_first.py` | Basic tests for arithmetic, strings, and lists. |
| `calculator.py` | Calculator functions for addition, subtraction, multiplication, and division. |
| `test_calculator.py` | Tests for calculator operations and the AAA pattern. |
| `test_exceptions.py` | Tests for exceptions using `pytest.raises()`. |

## Requirements

- Python 3
- pytest
- Git

## Installation

Install pytest:

```bash
python3 -m pip install pytest
```

## Running the Tests

Run all tests:

```bash
python3 -m pytest -v
```

Run a specific test file:

```bash
python3 -m pytest test_first.py -v
```

Run the calculator tests:

```bash
python3 -m pytest test_calculator.py -v
```

Run the exception tests:

```bash
python3 -m pytest test_exceptions.py -v
```

## Key Concepts

### 1. Assertions

Assertions check whether actual results match expected results.

```python
assert 1 + 1 == 2
```

### 2. Test Naming

pytest automatically discovers test files named `test_*.py` and test functions beginning with `test_`.

### 3. AAA Pattern

- **Arrange:** Prepare the test data.
- **Act:** Execute the function.
- **Assert:** Verify the result.

### 4. Exception Testing

Use `pytest.raises()` to verify that a function raises the expected exception.

## Expected Outcome

After completing this lab, students should be able to write and run basic automated tests, test calculator functions, interpret test results, and verify expected exceptions using pytest.

## Conclusion

This lab establishes the foundation for automated software testing with Python and pytest. These skills help developers identify bugs early and verify that their code behaves as expected.