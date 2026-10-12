# Contributing Guide

Thank you for helping improve LangGraph Zero to Advanced.

This repository prioritizes conceptual clarity, runnable examples, reliable tests, and progressive learning. Contributions should help learners understand both how a system works and why its design is appropriate.

## Development environment

Requirements:

- Python 3.13 or compatible version.
- `uv`.
- Git.
- A code editor.

Set up the environment from the repository root:

```bash
uv sync
```

Run Python commands with:

```bash
uv run python --version
```

Do not commit `.venv/`, local `.env` files, credentials, or generated artifacts.

## Lesson structure

Every practical lesson should contain three corresponding files.

1. **Python implementation:** runnable, typed, focused code.
2. **Markdown explanation:** a matching explanation beside the implementation.
3. **Dedicated test:** an automated test in the root `tests/` directory.

For example:

```text
01-core-graph-model/
├── 01_state.py
└── 01_state.md

tests/
└── test_01_state.py
```

The Markdown lesson must link to its implementation and test. The phase README must link to the Markdown lesson.

Conceptual-only lessons are permitted when a runnable implementation would be artificial. Such lessons must be explicitly classified and have a meaningful way to verify understanding.

## Lesson documentation

A practical lesson should explain:

- Learning objectives and prerequisites.
- The problem being solved.
- A real-world analogy where useful.
- The concept and relevant API.
- A small example and a source walkthrough.
- Exact execution commands and expected behavior.
- Automated tests and what they verify.
- Relevant failure cases, common mistakes, and debugging.
- Hands-on exercises and key takeaways.
- Links to relevant official documentation and the next lesson.
- Important limitations and concepts not yet covered.

Avoid repetitive explanations and unnecessary abstractions.

## Python and API standards

- Use readable, modern Python with type annotations.
- Keep functions focused and examples runnable.
- Use explicit input and output contracts.
- Handle errors intentionally.
- Avoid hard-coded secrets and machine-specific paths.
- Keep dependencies minimal.
- Verify framework APIs against current official documentation.
- Distinguish framework-specific behavior from general Python concepts.
- Explain significant architectural decisions and their trade-offs.

## Testing standards

Use Python `unittest` initially.

Tests should verify observable behavior, not merely that a function executes. Add relevant positive, negative, boundary, and error cases.

Run an individual test from the repository root:

```bash
uv run python -m unittest discover -s tests -p "test_01_state.py" -v
```

Run the full suite:

```bash
uv run python -m unittest discover -s tests -v
```

LLM-dependent tests must use mocks or deterministic fakes by default. The normal test suite must not require API credentials, incur API charges, or depend on network availability.

## Dependencies and configuration

Use `uv` to manage dependencies and keep `pyproject.toml` and `uv.lock` consistent.

Introduce framework dependencies only when the corresponding lessons require them.

Never commit real API keys, passwords, access tokens, or private configuration. Use `.env.example` for placeholders and keep `.env` ignored.

## Curriculum consistency

When changing a lesson, review its implementation, Markdown explanation, test, execution commands, expected output, and phase index.

Update imports, links, and curriculum-tracker entries when files change.

Do not mark a lesson complete until its implementation, documentation, and tests have been verified.

## Git workflow

Before committing:

1. Inspect `git status`.
2. Stage only the intended paths explicitly.
3. Review the staged diff.
4. Run relevant tests and validation commands.
5. Verify the effective author and committer identities.
6. Confirm that no secrets or unintended files are staged.

Use a GitHub-provided noreply email for public commit metadata. Never use a company email. Do not rewrite published history or force-push without explicit approval.

Before pushing, inspect the latest commit metadata and working-tree status.

## Pull requests and review

Keep contributions focused. Explain the problem, the chosen approach, relevant trade-offs, test results, and any limitations.

Changes should be understandable to beginners without sacrificing technical accuracy.

## License

The repository's license will be documented once the project owner has selected an appropriate license.