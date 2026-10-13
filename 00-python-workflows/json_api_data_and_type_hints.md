# Lesson 12 — JSON, API-Shaped Data and Type Hints

## 1. Learning objectives

By the end of this lesson, you should be able to:

- Convert JSON text into Python data using `json.loads()`.
- Convert Python data into JSON text using `json.dumps()`.
- Validate API-shaped input before processing it.
- Use basic type hints to communicate expected input and output types.
- Write tests for malformed JSON and invalid field values.

## 2. Why this lesson matters

Real applications exchange data between components and services. For example, a GitHub API may return information about a pull request (PR), and an AI application may send structured data to an LLM or receive structured output from it.

Python dictionaries and JSON text are related, but they are not the same thing. JSON is a data-interchange format; a Python dictionary is an in-memory Python object.

## 3. JSON serialization and parsing

### Python dictionary to JSON text

Use `json.dumps()`:

```python
import json

pr = {
    "number": 42,
    "title": "Fix login validation",
    "changed_files": 3,
}

payload = json.dumps(pr)
print(payload)
```

### JSON text to Python data

Use `json.loads()`:

```python
parsed = json.loads(payload)
print(parsed)
print(type(parsed).__name__)
```

For a JSON object, `json.loads()` produces a Python dictionary.

Remember:

- `dumps` serializes Python data into JSON text.
- `loads` parses JSON text into Python data.

## 4. Validate external input

Parsing JSON only tells us whether the text is valid JSON. It does not guarantee that the data has the fields or values our application requires.

Our PR payload expects:

| Field | Requirement |
|---|---|
| `number` | Positive integer |
| `title` | Non-empty string |
| `changed_files` | Non-negative integer |

The lesson implementation uses `parse_pr_payload()` to parse and validate the input before returning a normalized dictionary.

It rejects malformed JSON, non-object JSON values, missing or invalid fields, and blank titles.

### A subtle Python detail

In Python, `bool` is a subclass of `int`. Therefore, a check such as `isinstance(True, int)` returns `True`.

For fields that must contain an actual integer, this lesson uses:

```python
type(number) is int
```

That prevents JSON `true` from being accepted as PR number `1`.

## 5. What type hints do—and do not do

Consider:

```python
def parse_pr_payload(payload: str) -> dict[str, object]:
    ...
```

The annotations communicate that:

- `payload` is expected to be a string.
- The returned value is expected to be a dictionary with string keys and values represented by the broad `object` type.

Type hints improve readability and support static analysis. Python does not automatically enforce them at runtime. The explicit validation checks are what reject invalid values.

## 6. Serialization is not validation

`json.dumps()` converts supported Python values into JSON text. It does not enforce the business rules for a PR payload.

That is why parsing and validation are separate from serialization in this lesson. Applications should validate data at trust boundaries instead of assuming that its shape is correct.

## 7. Tests and expected behavior

Run the focused test suite:

```bash
python -m unittest discover -s tests -p "test_json_api_data_and_type_hints.py" -v
```

The eight tests cover:

1. Parsing a valid payload and trimming the title.
2. Serializing data and checking the round trip.
3. Rejecting malformed JSON.
4. Rejecting JSON arrays when an object is required.
5. Rejecting a missing PR number.
6. Rejecting a boolean PR number.
7. Rejecting a blank title.
8. Rejecting negative `changed_files`.

## 8. Connection to the next layers

These Python fundamentals prepare us for the next stages of the curriculum:

- **Direct LLM SDKs:** construct request payloads and inspect responses.
- **Structured model outputs:** parse and validate data returned by a model.
- **LangChain:** work with structured inputs and outputs across components.
- **LangGraph:** represent validated data in workflow state.
- **Langfuse:** trace application executions and investigate failures.

Each layer builds on the same principle: data should have a clear shape, and assumptions about external input should be checked.

## 9. Exercises

1. Add a `repository` field and require it to be a non-empty string.
2. Write a test that rejects a PR number of `0`.
3. Write a test that rejects a string such as `"three"` for `changed_files`.
4. Explain why type hints alone do not replace runtime validation.
5. Explain the difference between `json.loads()` and `json.dumps()` without looking at the code.

## 10. Key takeaways

- JSON is a data-interchange format, not a Python dictionary.
- `json.loads()` parses JSON text; `json.dumps()` serializes Python data.
- Valid JSON can still contain invalid application data.
- Type hints document expected types but do not automatically enforce them.
- Validate data before passing it deeper into an application or workflow.
