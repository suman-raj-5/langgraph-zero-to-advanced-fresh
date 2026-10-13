
# Lesson 7 — State Mutation vs. State Updates

## Learning objectives

By the end of this lesson, you should be able to:

- Explain mutation of a shared Python dictionary.
- Explain how returning a dictionary differs from mutating one.
- Apply returned updates explicitly using `dict.update()`.
- Test object identity, side effects, and final workflow results.
- Explain how this prepares us for LangGraph state updates.

## 1. The problem

In Lesson 6, workflow functions modified a shared state dictionary directly.

For example:

```python
state["status"] = "analyzed"
```

This changes the original dictionary. Other functions using that same dictionary can observe the change.

This is mutation.

## 2. Approach A — Shared mutation

Our `analyze_with_mutation()` function modifies the input state directly and returns that same object.

```python
result = analyze_with_mutation(state)

assert result is state
```

The `is` operator checks object identity. It verifies that both variables refer to the same object.

### Benefits

- Simple for small sequential workflows.
- Changes are immediately visible to other functions holding the same dictionary.

### Risks

- A function can change data without the caller explicitly applying an update.
- Side effects become harder to reason about as workflows grow.
- Multiple functions modifying the same state can make debugging more difficult.

## 3. Approach B — Return updates

Our `analyze_with_updates()` function returns a new dictionary containing only the fields it wants to update.

```python
update = analyze_with_updates(state)
```

The original state remains unchanged.

The caller can explicitly apply the update:

```python
state.update(update)
```

This adds new keys and overwrites existing keys when their names match.

Returning an update does not automatically merge it into the original state.

## 4. Compare the approaches

| Property | Shared mutation | Returned updates |
|---|---|---|
| Modifies input state | Yes | No |
| Returns the same object | Yes | No; returns an update dictionary |
| Caller controls when changes apply | Less explicitly | Yes |
| Final result can be equivalent | Yes | Yes |

Both approaches can produce identical final dictionary values. Their behavior and side effects are still different.

## 5. Why this matters for LangGraph

LangGraph nodes commonly return state updates instead of directly mutating the shared graph state.

The graph runtime applies those updates. Reducers define how updates are combined for state fields that need special merging behavior.

This gives us a useful mental model:

1. A workflow node reads state.
2. The node computes a result.
3. The node returns an update.
4. The graph applies the update according to its state and reducer rules.

Our Python example demonstrates the basic idea, but it is not a complete implementation of LangGraph's runtime or reducer behavior.

## 6. Tests and verification

Run the focused tests:

```bash
python -m unittest discover -s tests -p "test_state_mutation_vs_updates.py" -v
```

The tests verify:

- Mutation changes the original dictionary.
- Returning an update leaves the original dictionary unchanged.
- Applying an update changes the state.
- Both workflow implementations produce equivalent final results.

## 7. Key takeaway

**Mutation changes an existing object; returning an update describes changes that the caller can choose to apply.**

This distinction becomes increasingly important when workflows have many nodes, retries, parallel execution, persistence, and recovery.
