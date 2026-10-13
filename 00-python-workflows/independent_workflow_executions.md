
# Lesson 9 — Independent Workflow Executions

## Learning objectives

By the end of this lesson, you should be able to:

- Explain why mutable default arguments can cause state leakage.
- Create independent state for each workflow execution.
- Distinguish intentional mutation from unintended shared state.
- Test object identity and state isolation.
- Explain why isolation matters for concurrent and multi-tenant systems.

## 1. The problem

Our AI PR Review system may process multiple pull requests independently.

Suppose PR A contains a security finding and PR B is a documentation update. PR B must not inherit PR A's findings.

A common Python mistake is using a mutable object as a default argument:

```python
def create_review_state(title, findings=[]):
    findings.append(f"Reviewed: {title}")
    return {"title": title, "findings": findings}
```

Python creates that default list once when the function is defined. Calls that omit `findings` reuse the same list.

Consequently, changes made during one call can become visible during later calls.

## 2. The fix — create fresh mutable state

Use `None` as the default and create a new list inside the function:

```python
def create_review_state(title, findings=None):
    if findings is None:
        findings = []

    return {
        "title": title,
        "findings": findings,
        "status": "started",
    }
```

When no list is supplied, each call creates its own list.

We use `is None` because we want to create a new list only when no list was provided. An explicitly supplied empty list should remain the caller's list.

## 3. Intentional mutation is not the problem

Our `add_finding()` function modifies the state it receives:

```python
def add_finding(state, finding):
    state["findings"].append(finding)
    state["status"] = "analyzed"
    return state
```

This mutation is intentional. The function updates the review it was given.

The problem would be accidentally sharing that review's mutable state with another independent execution.

## 4. Independent workflow executions

Our `run_review()` function creates a fresh state for each run.

```python
review_a = run_review(
    "Authentication fix",
    "Hardcoded secret detected",
)

review_b = run_review("Documentation update")
```

PR A contains its security finding. PR B starts with an empty findings list.

Each review owns its state, so updates to one review do not affect the other.

## 5. Tests and verification

Run the focused tests:

```bash
python -m unittest discover -s tests -p "test_independent_workflow_executions.py" -v
```

The four tests verify:

1. Separate findings lists.
2. No finding leakage between reviews.
3. Mutations affect only the targeted review.
4. Each review starts with its own state dictionary.

## 6. Connection to later topics

**Direct LLM SDKs:** Each request should use the intended conversation context rather than accidentally reusing another request's mutable data.

**LangGraph:** Thread identifiers and checkpointing help manage graph execution state. Correct state ownership and isolation remain important.

**Concurrency:** Simultaneous executions need clear state boundaries. Shared mutable objects can create race conditions.

**Multi-tenant production systems:** One tenant's execution must not accidentally expose another tenant's findings or intermediate data.

Fresh Python objects are one part of isolation; they do not, by themselves, guarantee complete application-level or tenant-level security.

## 7. Key takeaway

**Create mutable state per independent execution. Mutate that state intentionally, and avoid sharing it accidentally.**
