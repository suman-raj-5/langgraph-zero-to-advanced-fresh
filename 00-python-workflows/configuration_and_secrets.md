# Lesson 10 — Modules, Configuration and Secrets

## Learning objectives

By the end of this lesson, you should be able to:

- Read configuration from environment variables.
- Explain why environment variables are strings.
- Apply defaults to optional configuration.
- Validate required settings and numeric values.
- Keep configuration separate from application logic.
- Test configuration without depending on the machine's environment.
- Explain the difference between configuration and secrets.

## 1. Why configuration matters

Imagine an AI PR reviewer running in three environments:

- Local development
- Testing
- Production

Each environment might use different model settings or retry limits.

Hard-coding these values into application logic makes the application harder to configure and maintain.

Instead, the application reads configuration from its environment.

## 2. Environment variables

Python provides `os.getenv()` to read environment variables.

```python
import os

model_name = os.getenv("MODEL_NAME")
max_retries = os.getenv("MAX_RETRIES", "2")
```

Important observations:

- A missing variable returns `None` unless a default is provided.
- The default for `MAX_RETRIES` is the string `"2"`.
- Values read from environment variables are strings.
- Environment variables are one way to configure an application; they are not the only possible configuration mechanism.

## 3. Convert and validate values

A retry count must be an integer.

```python
max_retries = int(max_retries_value)
```

However, conversion alone is not sufficient.

- `"3"` converts successfully.
- `"abc"` raises `ValueError`.
- `"-1"` converts successfully but may violate the application's rules.

Our implementation therefore separates conversion from business-rule validation.

It also rejects missing or whitespace-only model names.

## 4. Configuration versus secrets

**Configuration** controls application behavior. Examples include model names and retry limits.

**Secrets** grant access to protected systems. Examples include API keys, database passwords, and access tokens.

Both should be kept out of hard-coded application logic. Secrets require particular care because accidentally committing them can expose access to external services.

For local development, a `.env` file is a common option when the application uses a suitable environment-variable loader. This lesson does not require a `.env` file or any third-party package.

The repository's `.gitignore` excludes `.env` files while allowing example environment files.

An `.env.example` file should contain placeholders, never real credentials.

## 5. How the implementation works

Open `configuration_and_secrets.py`.

The `load_config()` function:

1. Reads `MODEL_NAME` and `MAX_RETRIES`.
2. Applies a default retry count of two when the retry variable is absent.
3. Rejects a missing or blank model name.
4. Converts the retry count to an integer.
5. Rejects invalid or negative retry counts.
6. Returns a dictionary containing validated configuration.

The `main()` function prints the non-secret settings. The main guard prevents the application from running automatically when the module is imported for testing.

## 6. Automated testing

Open `tests/test_configuration_and_secrets.py`.

The tests use `unittest` and `unittest.mock.patch.dict()`.

Passing `clear=True` creates a controlled environment for each test. This prevents unrelated environment variables from influencing the results.

The test suite covers:

- Valid configuration
- Default retry count
- Missing model name
- Blank model name
- Non-integer retry count
- Negative retry count

Run the focused tests:

```bash
python -m unittest discover -s tests -p "test_configuration_and_secrets.py" -v
```

## 7. Connection to the AI engineering stack

This lesson establishes a foundation for later technologies:

- **Direct LLM SDKs:** provide API credentials and model settings.
- **LangChain:** separates model configuration from application logic.
- **LangGraph:** uses configuration and runtime context to control workflow execution.
- **Langfuse:** uses credentials and configuration to enable observability.

These tools solve different problems. Environment-variable handling is a Python foundation, not a replacement for their specific configuration APIs.

## 8. Exercises

### Exercise A — Change the default

Change the default retry count from two to three. Update the test to verify the new default.

### Exercise B — Reject zero retries

Decide whether zero retries should be allowed in your application. If not, update the validation and add a test.

Explain the difference between a retry count of zero and a negative retry count.

### Exercise C — Add a timeout

Add a `TIMEOUT_SECONDS` setting with a reasonable default. Convert it to a numeric type and reject invalid values.

Decide whether zero or negative timeouts should be allowed.

### Exercise D — Protect secrets

Explain why an API key should not be printed, committed to Git, or placed in `.env.example`.

Do not use a real API key in these exercises.

## 9. Completion checklist

- [ ] Understand missing environment variables and defaults.
- [ ] Understand string conversion and validation.
- [ ] Distinguish configuration from secrets.
- [ ] Run all six focused tests.
- [ ] Complete the documentation and exercises.
- [ ] Run the full test suite before committing.

## Key takeaway

Configuration is external input. Read it deliberately, validate it at the application boundary, keep secrets out of source control, and test both valid and invalid settings.