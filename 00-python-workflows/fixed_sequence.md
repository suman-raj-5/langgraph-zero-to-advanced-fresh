
# Lesson 2: Fixed Sequences and Conditional Decisions

## Learning objectives

By completing this lesson, you should be able to:

- Explain how a sequence of Python functions forms a workflow.
- Use an `if`/`else` statement to choose between actions.
- Separate a decision from the action that follows it.
- Test a decision function independently using `unittest`.

## 1. The problem

Our first workflow collected pull-request details, analyzed the description,
and generated a summary.

That fixed sequence worked because every step followed the same path.

However, a review workflow may discover a security issue. In that situation,
we want to generate a security warning rather than a normal review summary.

## 2. The fixed sequence

The workflow initially followed these steps:

1. Collect pull-request details.
2. Analyze the pull request.
3. Generate a review summary.

The `run_workflow()` function coordinated these calls.

This approach is straightforward, but the workflow becomes harder to maintain
when different outcomes require different actions.

## 3. Conditional decisions

Python's `if` and `else` statements let a workflow choose between alternatives.

For example:

```python
if "security issue" in analysis.lower():
    summary = f"Security warning: {analysis}"
else:
    summary = generate_summary(analysis)
```

If the analysis contains "security issue", the workflow creates a security
warning. Otherwise, it generates the normal summary.

Only the selected branch executes.

## 4. Separate decisions from actions

We introduced this function:

```python
def choose_review_action(analysis):
    if "security issue" in analysis.lower():
        return "security_warning"

    return "normal_summary"
```

The function decides which action should run. It does not generate the
review summary itself.

The workflow then uses the returned value to choose the action.

This separation makes the decision logic easier to test and understand.

## 5. Automated tests

The tests in `tests/test_fixed_sequence.py` verify two cases:

- A security issue selects `security_warning`.
- A normal analysis selects `normal_summary`.

Run all project tests from the repository root:

```bash
uv run python -m unittest discover -s tests -v
```

Expected result: six tests pass, including the four tests from Lesson 1.

## 6. Limitations discovered

This is still ordinary Python workflow code.

As the workflow grows, we may need additional logic for:

- More possible decisions.
- Failed steps and retries.
- Sharing information across many steps.
- Tracking execution progress.
- Resuming after a failure.

Separating decision logic improves readability, but it does not automatically
provide these workflow-management capabilities.

## 7. Hands-on exercises

1. Change the analysis text to use `SECURITY ISSUE` in uppercase.
   Confirm that the decision function still selects `security_warning`.

2. Add a third action called `request_changes` for an analysis containing
   the phrase `needs changes`.

3. Write a test for the new decision.

4. Explain why the decision function is easier to test independently than
   the entire workflow.

## Key takeaway

Ordinary Python functions and conditionals are enough for small workflows.
Separating decisions from actions improves organization and testability.
Larger workflows introduce additional challenges that we will explore
before moving to LangGraph.

## Related files

- Implementation: `fixed_sequence.py`
- Tests: `../tests/test_fixed_sequence.py`
- Previous lesson: `sequential_workflow.md`
