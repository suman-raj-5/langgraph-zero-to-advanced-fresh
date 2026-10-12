# Lesson 4 — Workflow Failures and Retries

## Learning objectives

By completing this lesson, you will understand how to:

- Handle exceptions with `try` and `except`.
- Understand why a failed operation can stop a workflow.
- Retry a failed operation a limited number of times.
- Stop a workflow when a required operation fails.
- Generate a review summary only after the required security check succeeds.

## 1. Why failures matter

A workflow executes multiple steps in sequence. If a required step fails, the remaining steps may not execute.

In our pull request review example, the workflow:

1. Collects pull request details.
2. Analyzes the pull request.
3. Runs a security check.
4. Generates a review summary.

If the security check fails, the workflow should not generate a summary that implies the review completed successfully.

## 2. Handling exceptions

Python provides `try` and `except` to handle expected exceptions.

```python
try:
    run_security_check()
except RuntimeError as error:
    print(f"Security check failed: {error}")
```

- `try` contains the operation that may fail.
- `except RuntimeError` handles a `RuntimeError`.
- `error` provides access to the exception message.

Handling an exception prevents that specific failure from propagating out of the `try` block. The program must still decide whether to retry, stop, or take another action.

## 3. Retrying an operation

Temporary failures may resolve on a later attempt. Our example allows two attempts:

```python
for attempt in range(2):
    try:
        run_security_check()
        break
    except RuntimeError as error:
        print(f"Security check failed: {error}")
```

`range(2)` produces two loop iterations. `break` stops the loop after a successful security check.

The complete workflow also tracks whether the check succeeded. If both attempts fail, it stops without generating the review summary.

## 4. Failure scenarios

### Scenario A — First attempt fails, second succeeds

The workflow retries the security check and generates the summary after the successful attempt.

### Scenario B — Both attempts fail

The workflow reports that the security check could not be completed and exits without generating the summary.

## 5. Important production considerations

This lesson uses a simulated service failure. It does not contact a real security service.

Real retry policies should consider:

- Which failures are temporary and worth retrying.
- A maximum attempt count.
- Delays or exponential backoff between attempts.
- Timeouts and overall execution deadlines.
- Logging and observability.
- Whether repeating an operation is safe.
- Whether a required security check has actually passed.

A retry is not a substitute for handling a persistent failure.

## 6. Limitations of this example

The example uses a module-level counter to simulate a failure on the first attempt. This keeps the demonstration simple, but module-level mutable state can make repeated executions and tests harder to isolate.

Later lessons can introduce cleaner ways to manage workflow state and execution.

## 7. Run the example

From the repository root:

```bash
uv run python 00-python-workflows/workflow_failures.py
```

Run the test suite:

```bash
uv run python -m unittest discover -s tests -v
```

## Recap

A reliable workflow does not simply continue after a required operation fails. It handles expected exceptions, retries within a defined limit, and stops when the required operation cannot be completed successfully.