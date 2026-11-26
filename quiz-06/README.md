# Lab 06: Mocking and Test Doubles

**Course:** 192-211 Automated Software Testing  
**Institution:** International College, Siam University  
**Language:** Python 3  
**Testing Framework:** pytest  

## 1. Introduction

The purpose of this lab was to understand how mocking and test doubles help us test Python programs without depending on real external services.

External dependencies such as payment gateways, databases, email services, network connections, time, and random values can make tests slow, unreliable, or difficult to control.

By using `unittest.mock`, we can replace these dependencies with mock objects and control their behavior during testing.

## 2. Lab Objectives

The main objectives were:

- Understand when and why mocking is necessary.
- Create Mock objects and configure their return values.
- Patch functions and methods during tests.
- Verify how dependencies are called.
- Simulate exceptions and failures.
- Test retry behavior using `side_effect`.
- Control time-dependent behavior during testing.

## 3. Lab Activities

### Step 1: Understanding Why Mocking Is Needed

We started with a weather example using `get_temperature()` and `describe_weather()`.

The first test checked whether the weather description belonged to a list of possible answers. However, this test was weak because it did not verify the exact result for a particular temperature.

We then used `patch()` to control the temperature.

For example:

- When the temperature was 30, the result should be `"Hot"`.
- When the temperature was -5, the result should be `"Freezing"`.

This made the tests more accurate and predictable.

**Key learning:** Mocking allows us to control unpredictable dependencies and test specific behavior.

### Step 2: Mock Objects and Return Values

We used `Mock()` to create fake objects and configure their behavior.

We practiced:

- Setting a return value using `.return_value`.
- Calling mock methods.
- Assigning attributes to mock objects.
- Passing a mock payment gateway into `OrderProcessor`.

In the payment example, the mock gateway returned `"SUCCESS-12345"` without contacting a real payment service.

**Key learning:** Dependency injection allows a class to receive its dependencies from outside, making it easier to test.

### Step 3: Patching Dependencies and Methods

We practiced replacing functions and methods temporarily using `patch()` and `patch.object()`.

We also learned the important rule:

**Patch where the object is used, not where it is originally defined.**

Using `patch.object()`, we replaced the `charge()` method of `PaymentGateway` while keeping the rest of the real object.

**Key learning:** Patching allows us to replace specific dependencies during a test without changing the original implementation permanently.

### Step 4: Verifying Mock Interactions

In this step, we learned that checking a function's return value is not always enough.

Sometimes we need to verify whether a dependency was called correctly.

We practiced:

- `assert_called()`
- `assert_called_once()`
- `assert_called_with()`
- `assert_called_once_with()`
- `assert_not_called()`
- `call_count`

For example, we verified that the payment gateway was charged exactly once with an amount of 250.

We also tested invalid payment amounts to ensure the gateway was not called.

**Key learning:** Mock assertions help verify interactions between components, including calls that should never happen.

### Step 5: Exceptions and Side Effects

We practiced using `side_effect` to simulate different situations.

We tested:

- Raising a `ConnectionError`.
- Simulating two failures followed by a successful payment.
- Checking the number of retry attempts.
- Mocking the system clock using `patch("time.time")`.
- Using a function as `side_effect` to return different results based on the input.

For the retry example, the first two payment attempts failed, and the third attempt succeeded.

**Key learning:** `side_effect` can simulate exceptions, sequences of results, and dynamic behavior.

## 4. Test Results

After completing the exercises and correcting the payment implementation, I ran the complete test suite using:

```bash
pytest -v
```

The final result was:

```text
19 passed
```

All 19 collected tests passed successfully.

The tests covered:

- Mock basics
- Mock exceptions
- Mocking time
- Notifications
- Patching methods
- Payment processing
- Weather testing
- Retry behavior
- Dynamic side effects
- Verifying mock calls

## 5. Review Questions

### Question 1: Why should you mock a payment gateway in tests? Give two distinct reasons.

We should mock a payment gateway because we do not want tests to charge real money. It also makes tests faster and more reliable because they do not depend on an internet connection or an external payment service.

### Question 2: What is the difference between `return_value` and `side_effect`?

`return_value` gives the mock the same predefined result whenever it is called. `side_effect` is more flexible because it can raise an exception, return different values in sequence, or execute a function.

### Question 3: Module app does `import requests` and calls `requests.get`. What do you patch?

We should patch `app.requests.get` because the function is used through the `requests` module inside `app`.

### Question 4: Why can a mistyped assertion method make a test pass, and how do you prevent it?

A normal Mock can create unknown attributes automatically. Therefore, if we mistype an assertion method, it may return another Mock instead of producing an error. We can prevent this by using `Mock(spec=RealClass)` or `autospec=True` when patching.

### Question 5: Name one thing you should NOT mock, and say why.

We should not mock simple pure functions because they are already fast, predictable, and easy to test. Mocking them unnecessarily can make tests more complicated and dependent on implementation details.

## 6. Conclusion

In this lab, I learned how to use mocking and test doubles to test Python programs without relying on real external services.

I practiced creating mock objects, configuring return values, patching dependencies, verifying method calls, and simulating failures using `side_effect`.

I also learned that good unit tests should be fast, reliable, deterministic, and focused on the behavior being tested.

Overall, completing this lab helped me understand how mocking makes automated software testing easier and more effective.

---

**Test Status:** 19 tests passed successfully.