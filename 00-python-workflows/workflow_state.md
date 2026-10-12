# Lesson 6 — Explicit Workflow State

## Learning objectives

By completing this lesson, you will understand how to:

- Represent workflow information using a Python dictionary.
- Create an initial state.
- Read and update shared state across multiple functions.
- Preserve earlier information while adding new results.
- Track workflow progress using a status field.
- Test state updates and the complete workflow.

## 1. What is workflow state?

A workflow needs information to move between its steps. In this lesson, we represent that information using one Python dictionary called `state`.

Our pull request review workflow tracks:

- `title`: the pull request title.
- `description`: the pull request description.
- `status`: the current workflow status.
- `assessment`: the result of analyzing the description.
- `summary`: the generated review summary.

## 2. Create the initial state

```python
def create_initial_state():
    state = {
        "title": "Fix login validation",
        "description": "Validate user input before login",
        "status": "started",
    }

    return state
```

The initial state contains the information available at the beginning of the workflow. The assessment and summary are added later.

## 3. Update the shared state

The analysis function receives the existing dictionary and updates it.

```python
def analyze_state(state):
    description = state["description"]

    if len(description) >= 20:
        assessment = "Sufficient description"
    else:
        assessment = "Description needs more detail"

    state["assessment"] = assessment
    state["status"] = "analyzed"

    return state
```

The function reads the description, calculates an assessment, and adds the result to the dictionary.

It also changes the status to `analyzed`.

## 4. Generate a summary

```python
def generate_summary_state(state):
    title = state["title"]
    assessment = state["assessment"]

    state["summary"] = f"PR Review: {title} - {assessment}"
    state["status"] = "completed"

    return state
```

The summary function reads information already stored in the state, adds the summary, and updates the status.

## 5. Coordinate the workflow

```python
def run_workflow():
    state = create_initial_state()
    analyze_state(state)
    generate_summary_state(state)

    return state
```

The workflow creates the state once and passes the same dictionary through each step.

The progression is:

1. `started`: the initial state is created.
2. `analyzed`: the assessment is added.
3. `completed`: the review summary is added.

## 6. Understand object identity

The tests use `assertIs(result, state)` to verify that the function returns the same dictionary object it received.

This demonstrates that the functions mutate the existing dictionary instead of returning a separate dictionary.

This is a Python design choice for this lesson, not a requirement for every workflow framework.

## 7. Run the example

From the repository root:

```bash
uv run python 00-python-workflows/workflow_state.py
```

Expected output:

```text
{'title': 'Fix login validation', 'description': 'Validate user input before login', 'status': 'completed', 'assessment': 'Sufficient description', 'summary': 'PR Review: Fix login validation - Sufficient description'}
```

## 8. Run the tests

Run the lesson tests:

```bash
uv run python -m unittest tests/test_workflow_state.py -v
```

Run the full test suite:

```bash
uv run python -m unittest discover -s tests -v
```

The tests verify initial state creation, state updates, short-description behavior, and the complete workflow.

## 9. Important distinction

This lesson uses a regular Python dictionary that functions mutate directly. Later, we will compare this approach with other ways to represent and update state.

LangGraph has its own state model and update behavior. Understanding dictionaries and shared information first gives us a foundation for learning that model.

## Recap

Workflow state is information that a workflow uses as it progresses. In this example, multiple functions read and update one dictionary, preserving earlier information and adding new results as execution continues.