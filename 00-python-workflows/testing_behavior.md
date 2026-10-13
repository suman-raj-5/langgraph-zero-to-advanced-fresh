# Lesson 11 — Testing Behavior and Failures

## Learning objectives

By the end of this lesson, you should be able to:

- Explain why workflows need tests for both success and failure.
- Use `unittest.mock.patch.object()` to replace dependencies.
- Control mock behavior with `return_value`.
- Verify function calls and their arguments.
- Verify that a function is not called when it should be skipped.
- Explain how mocking isolates workflow behavior from external dependencies.

## 1. Why this lesson matters

A workflow may depend on several functions or external services. Even if each component works independently, the workflow can still behave incorrectly when coordinating them.

For example, a pull request reviewer should not generate a review summary if its required security check fails.

Tests help us verify these decisions without calling real external services.

## 2. The example workflow

Open `testing_behavior.py`.

The example contains three functions:

- `run_security_check()` simulates a security-check dependency.
- `generate_summary(analysis)` generates a summary from analysis.
- `run_workflow()` coordinates the dependencies.

The workflow generates a summary only when the security check succeeds.

This example is intentionally small so we can focus on testing behavior rather than implementing a complete review system.

## 3. What is mocking?

Mocking temporarily replaces a dependency with a controllable test double.

Python's `unittest.mock.patch.object()` lets us replace an attribute on an existing object for the duration of a test.

For example:

```python
with patch.object(
    testing_behavior,
    "run_security_check",
    return_value=True,
) as mock_check:
    result = testing_behavior.run_workflow()
```

During this test, the workflow calls the mock rather than the original security-check function.

This makes it possible to control the dependency's response and inspect how it was used.

## 4. Control behavior with return_value

A mock's `return_value` determines what it returns when called.

In our tests:

- `return_value=True` simulates a successful security check.
- `return_value=False` simulates a failed security check.
- A mocked summary generator can return a predictable result such as `"Test summary"`.

This lets us test different workflow scenarios without modifying the implementation.

## 5. Verify calls and arguments

A test should verify more than the final output when the interactions themselves matter.

### Verify a call

```python
mock_check.assert_called_once()
```

This verifies that the dependency was called exactly once.

### Verify arguments

```python
mock_summary.assert_called_once_with(
    "Analysis complete for: Fix login validation"
)
```

This verifies that the summary generator received the expected analysis.

### Verify a function was not called

```python
mock_summary.assert_not_called()
```

This verifies that the workflow skipped summary generation when the security check failed.

These assertions help protect the contracts between workflow components.

## 6. Test isolation

The tests replace dependencies only while their `patch.object()` context managers are active. When the context ends, the original functions are restored.

This makes each test easier to control and reduces accidental interference between tests.

However, mocking does not prove that a real external service works. Integration tests are still needed to verify real service behavior.

## 7. Run the focused tests

From the repository root, run:

```bash
python -m unittest discover -s tests -p "test_testing_behavior.py" -v
```

The two tests cover:

1. Returning a summary after a successful security check.
2. Stopping summary generation after a failed security check.

## 8. Connection to AI engineering

These testing concepts transfer to later technologies:

- **Direct LLM SDKs:** mock model calls to test application behavior without making paid requests.
- **LangChain:** test how application components handle model and tool responses.
- **LangGraph:** test node behavior, routing decisions, and state-dependent execution.
- **Langfuse:** test application logic separately from observability integrations.

Mocking is a testing technique, not a replacement for validating the real SDK, model provider, or external service.

## 9. Exercises

### Exercise A — Change the analysis

Modify the workflow to use a different PR title. Update the test to verify the new analysis reaches the summary generator.

### Exercise B — Add another failure condition

Make the workflow stop when analysis is empty. Write a test that verifies the summary generator is not called.

### Exercise C — Design a test matrix

For an LLM dependency, identify how you would test:

- A valid response
- An exception
- An empty response
- An invalid response

Do not call a real paid API for these exercises.

## 10. Completion checklist

- [ ] Understand `patch.object()`.
- [ ] Control mock responses with `return_value`.
- [ ] Verify calls and their arguments.
- [ ] Verify that forbidden calls do not occur.
- [ ] Run the focused tests.
- [ ] Run the full regression suite.

## Key takeaway

Test the behavior of the workflow by controlling its dependencies, checking its outputs, and verifying which operations should—or should not—occur.