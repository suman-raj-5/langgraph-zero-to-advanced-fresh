
# Lesson 8 — Validation and Function Contracts

## Learning objectives

By the end of this lesson, you should be able to:

- Explain why Python does not automatically reject invalid application inputs.
- Define a simple function contract.
- Validate required dictionary fields and their types.
- Reject empty and whitespace-only strings.
- Raise clear exceptions for invalid input.
- Test successful validation and failure behavior.

## 1. The problem

Our AI PR Review workflow expects a PR title and description.

Consider this input:

```python
{
    "title": "",
    "description": None,
}
```

Python allows these values. An empty string and `None` are valid Python objects, even though they violate our workflow's requirements.

Without validation, invalid data could propagate into later workflow steps and cause misleading results or unexpected failures.

## 2. What is a function contract?

A function contract defines the expectations and guarantees associated with a function.

For our PR review workflow, the input contract is:

- The input must be a dictionary.
- `title` must be a non-empty string.
- `description` must be a non-empty string.
- Invalid inputs must raise a clear `ValueError`.
- Valid inputs must be returned unchanged by the validation function.

The contract gives callers a predictable way to use the function.

## 3. Type checking and content checking

We use `isinstance()` to check the type of a value.

```python
isinstance("Fix login validation", str)  # True
isinstance(None, str)                   # False
```

However, a string can still be empty or contain only whitespace.

```python
bool("")        # False
bool("   ")     # True
"   ".strip()   # ""
```

That is why our validation combines type checking with `.strip()`.

## 4. Reject invalid inputs explicitly

Our validation function raises `ValueError` when the contract is violated.

```python
if not isinstance(title, str) or not title.strip():
    raise ValueError("PR title must be a non-empty string")
```

This rejects missing values, non-string values, empty strings, and whitespace-only strings.

The same principle applies to the description.

## 5. Enforce validation before analysis

Our `analyze_pr()` function calls `validate_pr_details()` before processing the description.

This matters because callers might invoke `analyze_pr()` directly instead of going through `main()`.

Validation inside the function protects that boundary regardless of which caller invokes it.

## 6. Tests and verification

Run the focused tests:

```bash
python -m unittest discover -s tests -p "test_validation_and_contracts.py" -v
```

The eight tests cover:

1. Valid PR details.
2. A non-dictionary input.
3. A missing title.
4. A whitespace-only title.
5. A non-string description.
6. A whitespace-only description.
7. Validation before analysis.
8. Successful analysis of valid input.

## 7. Connection to the next layers

**Direct LLM SDKs:** Model responses and tool arguments also need validation before the application trusts or processes them.

**Structured outputs:** Schemas can constrain the shape and types of model-generated data. Application-level validation may still be needed for business rules.

**LangGraph:** State updates from nodes must satisfy the requirements of subsequent workflow steps.

**Production systems:** Clear contracts help isolate bad inputs, make failures predictable, and simplify debugging.

## 8. Key takeaway

**A function contract makes expectations explicit; validation enforces those expectations at runtime.**

Python permits many values that an application should not accept. Our code must define and enforce its own rules.
