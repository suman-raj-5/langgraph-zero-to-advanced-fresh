# Lesson 5 — Breaking a Workflow into Reusable Steps

## Learning objectives

By completing this lesson, you will understand how to:

- Separate a workflow into small, reusable functions.
- Give each function one clear responsibility.
- Pass information between functions using arguments and return values.
- Create a coordinator function that controls the execution sequence.
- Test individual functions and verify how a workflow connects them.

## 1. Why separate workflow steps?

A pull request review can involve collecting information, analyzing the changes, and generating a summary.

Putting every operation into one large function makes the workflow harder to understand, test, and maintain.

Instead, we give each operation its own function:

1. `collect_pr_details()` collects pull request information.
2. `analyze_pr(pr_details)` evaluates the description.
3. `generate_summary(analysis)` creates a readable summary.
4. `run_workflow()` coordinates the functions.

## 2. Collect information

The collection function returns a dictionary containing the pull request title and description.

```python
def collect_pr_details():
    pr_details = {
        "title": "Fix login validation",
        "description": "Validate user input before login",
    }

    return pr_details
```

The `return` statement sends the dictionary back to the caller.

## 3. Analyze the information

The analysis function receives the dictionary as an argument.

```python
def analyze_pr(pr_details):
    title = pr_details["title"]
    description = pr_details["description"]

    if len(description) >= 20:
        assessment = "Sufficient description"
    else:
        assessment = "Description needs more detail"

    return {
        "title": title,
        "assessment": assessment,
    }
```

The function doesn't collect the details itself. It receives them from its caller, which makes it reusable with different inputs.

## 4. Generate the summary

The summary function receives the analysis result and formats it into a string.

```python
def generate_summary(analysis):
    title = analysis["title"]
    assessment = analysis["assessment"]

    summary = f"PR Review: {title} - {assessment}"

    return summary
```

Formatting is separated from analysis. A change to the summary format does not require changing the analysis function.

## 5. Coordinate the workflow

The coordinator calls the functions in order and passes each result to the next step.

```python
def run_workflow():
    pr_details = collect_pr_details()
    analysis = analyze_pr(pr_details)
    summary = generate_summary(analysis)

    return summary
```

The data flows through the workflow as follows:

`collect_pr_details()` → `analyze_pr(pr_details)` → `generate_summary(analysis)`

The individual functions perform their responsibilities, while `run_workflow()` controls the sequence.

## 6. Program entry point

The program uses a `main()` function and a standard Python entry-point guard.

```python
def main():
    summary = run_workflow()
    print(summary)


if __name__ == "__main__":
    main()
```

The guard runs `main()` when the file is executed directly. Importing the module into a test does not automatically run `main()`.

## 7. Testing

Run the lesson directly:

```bash
uv run python 00-python-workflows/reusable_steps.py
```

Run the lesson's tests:

```bash
uv run python -m unittest tests/test_reusable_steps.py -v
```

Run the full test suite:

```bash
uv run python -m unittest discover -s tests -v
```

The tests verify individual function results, short-description behavior, the final summary, and the handoffs between workflow steps.

## 8. Key takeaways

- A function should have a clear responsibility.
- Arguments pass information into a function.
- Return values pass results back to the caller.
- A coordinator function organizes execution without duplicating each step's logic.
- Unit tests can verify both individual behavior and interactions between functions.

These concepts prepare us to understand how workflow steps and information flow will later be represented in LangGraph.