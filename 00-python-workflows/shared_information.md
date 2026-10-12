
# Lesson 3: Sharing Information Between Workflow Steps

## Learning objectives

By completing this lesson, you should be able to:

- Explain how functions pass information through arguments and return values.
- Understand why long argument lists can become cumbersome.
- Create a Python dictionary using key-value pairs.
- Pass a dictionary between functions.
- Test shared information and summary generation with `unittest`.

## 1. Passing information between functions

In ordinary Python, one function can return information that another function
receives through its arguments.

For example, our workflow collects a pull-request title and description, then
passes them to an analysis function.

This approach is explicit and works well when functions need only a few values.

## 2. The challenge of growing workflows

As the review workflow grows, it may need to carry:

- Pull-request title
- Description
- Changed files
- Test status
- Security findings

Passing each value separately is valid Python, but the argument lists can
become longer as more information is required.

## 3. Grouping related information in a dictionary

A dictionary stores information as key-value pairs.

For example:

```python id="88shw3"
pr_details = {
    "title": "Fix login validation",
    "test_status": "passed",
}
```

The keys label the information, and the values hold the corresponding data.

Our implementation collects five fields in a dictionary and returns it.

## 4. Accessing dictionary values

A function can retrieve a value using its key:

```python id="x2v8ps"
pr_details["title"]
```

This expression retrieves the pull-request title.

The key must exist in the dictionary. Otherwise, using square brackets
with a missing key raises a `KeyError`.

## 5. Passing a shared dictionary

Instead of passing several arguments, our workflow calls:

```python id="8c9g2u"
generate_summary(pr_details)
```

The summary function receives the dictionary and reads the fields it needs.

This groups related information together and reduces the number of arguments
that the caller must pass.

## 6. Trade-offs

Separate function arguments:

- Make a function's required values explicit.
- Work well when only a few values are needed.
- Can become cumbersome when many values must be passed.

A shared dictionary:

- Groups related information together.
- Lets different functions read the fields they need.
- Requires consistent key names and expected fields.
- Can fail at runtime if a required key is missing.

Neither approach is always best. Choose based on the size and needs of the workflow.

## 7. Automated tests

The tests in `tests/test_shared_information.py` verify that:

- The collector returns a dictionary.
- The summary contains the expected information.
- The complete workflow executes successfully.

Run all project tests from the repository root:

```bash id="hdm3zz"
uv run python -m unittest discover -s tests -v
```

Expected result: nine tests pass across Lessons 1, 2, and 3.

## 8. Hands-on exercises

1. Add a `reviewer` field to the dictionary.
2. Print the reviewer in the summary.
3. Add a test verifying that the reviewer appears in the output.
4. Remove the `test_status` key temporarily and observe what happens.
5. Explain when you would prefer separate arguments over a shared dictionary.

## Key takeaway

Function arguments and return values are the foundation of information sharing
in Python workflows. A dictionary provides a simple way to group related data
when multiple workflow steps need to use it.

This is ordinary Python state management, not LangGraph state yet.

## Related files

- Implementation: `shared_information.py`
- Tests: `../tests/test_shared_information.py`
- Previous lesson: `fixed_sequence.md`
