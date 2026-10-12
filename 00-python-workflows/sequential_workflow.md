# Lesson 1 — Building a Sequential Workflow with Python

## Learning objectives

By the end of this lesson, you should be able to:

- Explain what a workflow is.
- Understand how Python executes instructions in sequence.
- Create and call functions.
- Pass information using function arguments.
- Return results from functions.
- Use variables, strings, `len()`, and `if` statements.
- Explain how one function's output becomes another function's input.

## Prerequisites

You only need basic familiarity with Python, such as running a Python file and recognizing simple values and statements.

If functions or `return` are new to you, work through the explanations below slowly. You do not need to know LangChain or LangGraph.

## 1. What is a workflow?

A workflow is a series of steps performed to achieve a result.

Imagine reviewing a pull request in a software project. A pull request proposes changes to a codebase. Before reviewing its code, a system might collect its title and description, examine the description, and prepare a summary.

For this first lesson, we will simulate those steps with ordinary Python. We will not call an AI model or inspect actual source code.

Our workflow is:

1. Collect pull request details.
2. Analyze the description.
3. Generate a summary.

Each step has a specific responsibility, and the steps run in a fixed order.

## 2. The problem we are solving

Suppose we have this pull request:

- Title: `Fix login validation`
- Description: `Validate empty usernames and reject invalid login requests.`

We want the program to check the description length and produce a readable review summary.

This is a deterministic example: given the same inputs, the program follows the same instructions and produces the same result.

The description-length rule is only a teaching example. A real code review cannot be judged by description length alone.

## 3. Understand the important Python concepts

### Variables

A variable gives a name to a value.

```python
title = "Fix login validation"
```

Here, `title` refers to a string containing the pull request title. The quotation marks indicate a string value.

### Functions

A function groups instructions under a name so that we can call those instructions when needed.

```python
def collect_pr_details():
    title = "Fix login validation"
    description = "Validate empty usernames and reject invalid login requests."

    return title, description
```

The `def` keyword defines a function. The indented lines form its body.

When Python executes `return title, description`, the function sends both values back to its caller as a tuple. A tuple is a Python value that can contain multiple values in a fixed sequence.

### Function arguments

Arguments let us pass information into a function.

```python
def analyze_pr(description):
    description_length = len(description)
```

The function receives a value through `description`. The `len()` function counts the characters in this string.

### Conditional statements

An `if` statement allows a program to choose what to do based on a condition.

```python
if description_length < 30:
    return "The PR description needs more detail."

return "The PR description has enough detail."
```

If the length is less than 30, Python returns the first message. Otherwise, execution continues to the next `return` statement.

The comparison operator `<` means "less than."

### Return values

A `return` statement sends a result back to the code that called a function.

```python
def generate_summary(title, review):
    return f"Pull request: {title}\nReview: {review}"
```

An f-string lets us insert variable values into text. The `\n` creates a new line.

## 4. Walk through the implementation

The implementation is in [`sequential_workflow.py`](sequential_workflow.py).

### Step 1 — Collect the details

`collect_pr_details()` creates two strings and returns them.

```python
title, description = collect_pr_details()
```

Python assigns the first returned value to `title` and the second to `description`. This is called unpacking.

### Step 2 — Analyze the description

```python
review = analyze_pr(description)
```

The description is passed to `analyze_pr()`. That function counts its characters and returns one of two messages.

The returned message is assigned to `review`.

### Step 3 — Generate the summary

```python
summary = generate_summary(title, review)
```

This passes the title and review message to `generate_summary()`, which combines them into a single string.

### Step 4 — Coordinate the workflow

```python
def run_workflow():
    title, description = collect_pr_details()
    review = analyze_pr(description)
    summary = generate_summary(title, review)

    return summary
```

The function calls each step in sequence. Notice that the summary function does not need to know how the description was analyzed. It only needs the values passed to it.

This separation makes each function easier to understand and test.

### Step 5 — Run the program

The `main()` function calls the workflow and prints the result.

```python
def main():
    result = run_workflow()
    print(result)


if __name__ == "__main__":
    main()
```

The final condition is a standard Python pattern. When the file is run directly, Python calls `main()`. When another Python file imports this module, the `main()` function is not automatically called.

## 5. Run the lesson

From the repository root, execute:

```bash
uv run python 00-python-workflows/sequential_workflow.py
```

Expected output:

```text
Pull request: Fix login validation
Review: The PR description has enough detail.
```

The output confirms that the three processing steps completed and the workflow returned a summary.

## 6. How the data flows

```text
collect_pr_details()
        |
        | title, description
        v
analyze_pr(description)
        |
        | review message
        v
generate_summary(title, review)
        |
        | summary string
        v
run_workflow() returns the result
```

The workflow is sequential because the steps are called in a fixed order. Each step receives the information it needs from the previous step or from the workflow coordinator.

## 7. Common mistakes

### Forgetting to call a function

Writing `run_workflow` refers to the function itself. Writing `run_workflow()` calls it.

### Forgetting `return`

A function without an explicit `return` statement returns `None` by default. That may cause a later step to receive an unexpected value.

### Using a variable before assigning it

Python raises an error if a local variable is referenced before it has been assigned a value.

### Incorrect indentation

The body of a function and the body of an `if` statement must be indented consistently.

### Misunderstanding the length rule

`len()` counts characters, including spaces and punctuation in a string. The threshold of 30 is arbitrary and does not measure the actual quality of a pull request.

## 8. Hands-on exercises

Try these yourself before looking at any solution.

1. Change the pull request title to `Add password reset`.
2. Change the description to `Fix login errors.` and run the program again.
3. Change the condition from `< 30` to `< 15`. What changes?
4. Modify the summary to include the description length.
5. Add a new function that prints `Starting review...` and call it before collecting the details.

### Challenge

Without changing the order of the workflow, explain how you would add a step that checks whether the title is empty.

Focus on where that step belongs and what information it needs.

## 9. Key takeaways

- A workflow can be built with ordinary Python functions.
- Functions can separate responsibilities.
- Arguments pass information into functions.
- Return values pass results back to callers.
- A coordinator function can control the execution order.
- Simple workflows do not require an orchestration framework.

## 10. Limitations and next lesson

This workflow uses fixed inputs and a simple rule. It does not call an LLM, inspect actual code changes, persist state, or recover from interrupted execution.

In the next lesson, we will build a conditional workflow and explore how a program chooses between different paths.

Later, we will revisit these patterns to understand what changes when workflows need dynamic routing, shared state, persistence, retries, and more complex execution.

## References

- [Python tutorial — Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python documentation — Built-in functions](https://docs.python.org/3/library/functions.html)
- [Python tutorial — More on defining functions and tuples](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)

## Related files

- Implementation: [`sequential_workflow.py`](sequential_workflow.py)
- Dedicated test: `tests/test_sequential_workflow.py` (to be created)