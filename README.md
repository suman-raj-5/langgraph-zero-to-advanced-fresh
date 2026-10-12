# LangGraph Zero to Advanced

**A hands-on journey from Python fundamentals to advanced AI agent engineering and production architecture.**

This repository teaches AI application and agent engineering from the ground up. It is designed for learners with little or no previous experience who want to progress toward designing, implementing, testing, debugging, and operating reliable AI agent systems.

Rather than collecting disconnected code snippets, this project builds knowledge progressively through runnable Python implementations, detailed explanations, automated tests, practical exercises, and production-oriented examples.

## Learning philosophy: Understand the problem before the framework

This course does not begin by asking learners to memorize LangChain or LangGraph APIs. It begins with Python and gradually introduces each technology when a concrete engineering problem justifies it.

### 1. Python — What can we already build?

Python provides functions, data structures, loops, conditions, exception handling, and testing. These are enough to build many deterministic workflows.

As applications grow, however, developers may end up writing increasingly complex orchestration code, managing shared data manually, and handling retries, branching, and failures across multiple steps.

**What we learn:** Build workflows using plain Python and understand their strengths and limitations.

### 2. Direct LLM SDKs — How do we communicate with a model?

An LLM provider SDK allows an application to send requests to a model and receive responses. Developers must understand authentication, messages, structured responses, streaming, tool-call protocols, provider errors, and rate limits.

When an application uses multiple model providers or repeatedly implements similar integration logic, maintaining that code can become difficult.

**What we learn:** Invoke a model directly, inspect its response, handle failures, and test the integration without requiring live API calls in the default test suite.

### 3. LangChain — How do we build reusable LLM applications?

LangChain provides abstractions and integrations for working with chat models, messages, structured outputs, tools, retrieval, and other LLM application components.

It can reduce repetitive integration code and help developers compose reusable building blocks. It does not eliminate the need to understand Python, model behavior, security, or application architecture.

**What we learn:** Understand the problems LangChain solves, the abstractions it introduces, and when direct SDK usage is sufficient.

### 4. LangGraph — How do we control complex, stateful execution?

Complex applications may need explicit state transitions, conditional routing, loops, parallel execution, persistence, human approval, and recovery after interruption.

LangGraph provides graph-based orchestration for these workflows. It helps make execution and state transitions explicit, but developers must still design reliable business logic, handle side effects, and establish appropriate persistence and security boundaries.

**What we learn:** Build workflows that can be inspected, tested, resumed, and extended without relying on an uncontrolled collection of nested conditionals and function calls.

### 5. Langfuse — How do we understand and improve system behavior?

An AI application can execute successfully while still producing incorrect, expensive, slow, or inconsistent results. Ordinary application logs may not provide enough context to understand the complete model and tool execution path.

Langfuse provides observability and evaluation capabilities that help developers inspect traces, diagnose failures, manage prompts, and evaluate system behavior.

**What we learn:** Instrument applications, investigate failures, measure quality and performance, and use evidence to improve the system.

### 6. LangSmith — What is the alternative, and why choose Langfuse?

LangSmith offers tracing, evaluation, and development tooling, including integrations with the LangChain ecosystem. Langfuse provides an alternative with an open-source, self-hostable platform and capabilities for tracing, prompt management, and evaluation.

This course uses Langfuse as its primary observability learning platform. We will compare both tools using documented capabilities, integrations, deployment options, data-handling requirements, and costs rather than claiming that either platform is universally superior.

### 7. Production AI engineering — How do we make the system reliable?

A working demo is not automatically a production-ready system. Real applications must address configuration, authentication, authorization, persistence, concurrency, idempotency, retries, timeouts, observability, cost control, testing, deployment, and operational recovery.

PostgreSQL will be introduced when its role becomes meaningful, including application data, transactions, migrations, and suitable persistence integrations. We will distinguish application data from LangGraph checkpoints and other forms of state.

**What we learn:** Make architectural decisions based on requirements, failure modes, operational constraints, and measurable trade-offs.

### The central principle

We will not introduce a framework merely because it exists. We will first understand the problem, build the simplest useful solution, identify its limitations, and then evaluate whether a framework or additional component solves a real need.

Python, model SDKs, LangChain, LangGraph, Langfuse, LangSmith, and PostgreSQL serve different purposes. They are complementary tools, not mandatory layers in every application.

## Who is this for?

- Beginners starting their AI engineering journey.
- Python developers learning LLM application development.
- Developers learning LangChain, LangGraph, and tool-using agents.
- Engineers preparing to build stateful and multi-agent systems.
- Developers progressing toward production-level AI engineering and architecture.

No prior LangGraph or LangChain experience is required. Python fundamentals will be introduced before framework-specific concepts.

## How lessons work

Every practical lesson follows a consistent structure:

1. **Python implementation** — a runnable example with readable, typed code.
2. **Markdown explanation** — concepts, analogies, design decisions, source walkthroughs, expected behavior, mistakes, and exercises.
3. **Dedicated automated test** — verification of observable behavior, including relevant edge cases and failures.

A lesson is complete only when its implementation, documentation, tests, execution instructions, and expected behavior have been verified.

The course distinguishes between implementing a concept and understanding it. Exercises, debugging tasks, design trade-offs, and architecture questions help learners develop independent engineering judgment.

## Curriculum roadmap

| Phase | Subject |
|---|---|
| 00 | Python Workflows |
| 01 | Core Graph Model |
| 02 | Messages and LLM State |
| 03 | Control Flow |
| 04 | Persistence and Execution |
| 05 | Memory |
| 06 | Streaming |
| 07 | Human-in-the-Loop |
| 08 | Subgraphs and Architecture |
| 09 | Runtime and Context |
| 10 | Tools and Agents |
| 11 | Multi-Agent Systems |
| 12 | Production Engineering |
| 13 | Langfuse Observability |

The curriculum starts with Python workflow fundamentals and progresses through LangChain and LangGraph foundations into agent systems, production engineering, and observability. Supporting lessons will be added where necessary to establish prerequisites and deepen understanding.

See each phase's `README.md` for its lesson index as the curriculum develops.

## Technologies

- **Language:** Python
- **Environment and dependency management:** uv
- **LLM application framework:** LangChain
- **Graph orchestration:** LangGraph
- **Observability and evaluation:** Langfuse
- **Database and durable application data:** PostgreSQL, introduced when appropriate
- **Testing:** Python `unittest` initially
- **Development tools:** Git, Git Bash, and VS Code

We will verify framework APIs and dependency compatibility against official documentation as the relevant lessons are introduced. Dependencies will be added progressively rather than installing every package at the beginning.

## Environment setup

### Prerequisites

- Python 3.13 or a compatible version.
- [uv](https://docs.astral.sh/uv/) for environment and dependency management.
- Git and a code editor such as VS Code.

### Clone the repository

```bash
git clone https://github.com/suman-raj-5/langgraph-zero-to-advanced-fresh.git
cd langgraph-zero-to-advanced-fresh
```

### Set up the environment

```bash
uv sync
```

Run commands through the project environment:

```bash
uv run python --version
```

The initial environment intentionally has no unnecessary framework dependencies. Packages will be added as the curriculum reaches the concepts that require them.

## Running lessons and tests

Run a lesson from the repository root using its documented command. For example:

```bash
uv run python path/to/lesson.py
```

Run an individual lesson's test:

```bash
uv run python -m unittest discover -s tests -p "test_01_state.py" -v
```

Run the complete test suite:

```bash
uv run python -m unittest discover -s tests -v
```

Replace the example test filename with the relevant lesson's test file.

Each lesson's Markdown guide will explain its exact commands and expected output.

## PostgreSQL and persistence

PostgreSQL will be introduced when the curriculum reaches persistence and production engineering.

We will distinguish graph checkpoints from application data, explain threads and execution history, and demonstrate appropriate database boundaries. Later lessons will explore connection management, transactions, migrations, concurrency, recovery, and operational considerations where relevant.

The initial Python workflow and core graph lessons will not require a running PostgreSQL server.

## Langfuse and LangSmith

The primary observability learning track uses Langfuse to study tracing, debugging, prompt management, and evaluation.

LangSmith will also be discussed and compared. The objective is to understand both platforms, their integration options, operational trade-offs, and the circumstances in which each may be appropriate.

The choice of Langfuse is a curriculum decision, not a claim that one platform is universally superior.

## Security and configuration

- Never commit real API keys, passwords, tokens, or private credentials.
- Keep local `.env` files out of Git.
- Use `.env.example` for placeholder values only.
- Keep secrets out of source code, test fixtures, screenshots, logs, and public documentation.
- Use a GitHub-provided noreply email for public Git commit metadata.
- Verify author and committer identities before pushing.
- Use mocks or deterministic fake models in the default automated tests; tests should not require API credentials or incur API charges.

## Progress and completion

The curriculum tracker will record lesson prerequisites, learning objectives, implementation status, test status, documentation status, and completion criteria.

A lesson will not be marked complete merely because its files exist. Its behavior must be tested and its documentation checked against the implementation.

Follow the [curriculum tracker](docs/curriculum-tracker.md) to review lesson prerequisites, objectives, implementation progress, verification status, and mastery criteria.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the conventions governing lesson files, tests, documentation, and contributions.

## Official documentation

- [Python](https://docs.python.org/3/)
- [uv](https://docs.astral.sh/uv/)
- [LangChain](https://docs.langchain.com/oss/python/langchain/overview)
- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
- [Langfuse](https://langfuse.com/docs)
- [LangSmith](https://docs.langchain.com/langsmith/overview)
- [PostgreSQL](https://www.postgresql.org/docs/)

## Project status

**Foundation setup.** The repository and development environment are being established. Lessons, phase indexes, tests, and supporting documentation will be added incrementally and marked complete only after verification.