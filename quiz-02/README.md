# Lab 2: Writing Effective Test Cases

**Course:** 192-211 Automated Software Testing  
**University:** Siam University

## Overview

This lab focuses on writing effective test cases and understanding what makes a test valuable. It builds on the fundamentals of automated testing by emphasizing clear test structure, meaningful assertions, and effective test design.

## Learning Objectives

- Understand the characteristics of effective test cases.
- Write clear and descriptive test functions.
- Use assertions to verify expected behavior.
- Design test cases for different inputs and scenarios.
- Identify meaningful test cases that can detect bugs.
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

Run a specific test file:

```bash
python3 -m pytest test_effective_cases.py -v
```

## Characteristics of Effective Test Cases

### 1. Clear Test Names

Use descriptive function names that explain the behavior being tested.

### 2. Meaningful Assertions

Assertions should verify the expected behavior of the code.

### 3. Different Test Scenarios

Test normal inputs, boundary conditions, and invalid inputs when applicable.

### 4. Independent Tests

Each test should be understandable and should not depend unnecessarily on other tests.

### 5. Readable Test Structure

Use the Arrange, Act, Assert (AAA) pattern:

- **Arrange:** Prepare the test data.
- **Act:** Execute the function.
- **Assert:** Verify the result.

## Example

```python
def add(a, b):
    return a + b


def test_add_positive_numbers():
    # Arrange
    first_number = 2
    second_number = 3

    # Act
    result = add(first_number, second_number)

    # Assert
    assert result == 5
```

## Conclusion

Effective test cases help identify defects, verify expected behavior, and make automated tests easier to understand and maintain.