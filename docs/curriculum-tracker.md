# Curriculum Tracker

This document tracks the learning journey from Python fundamentals to advanced AI agent engineering. It is the source of truth for lesson status, prerequisites, file paths, verification, and learner mastery.

The curriculum is built incrementally. Future lessons may be planned before their files exist. A planned lesson is not an implemented or verified lesson.

## 1. Status definitions

### Implementation status

| Status | Meaning |
|---|---|
| Planned | Included in the curriculum but not implemented. |
| In Progress | Implementation or documentation work has started. |
| Implemented | The required files exist, but verification may be incomplete. |
| Verified | Implementation, documentation, tests, commands, and expected behavior have been checked. |

### Learning status

| Status | Meaning |
|---|---|
| Not assessed | The learner has not yet demonstrated the concept independently. |
| Practicing | The learner is working through exercises and debugging tasks. |
| Mastered | The learner can explain the concept, solve relevant exercises, diagnose failures, and justify design choices independently. |

Implementation and learning status are separate. A verified implementation does not automatically mean the learner has mastered the concept.

## 2. Foundation curriculum — Before advanced graph lessons

These foundations establish why each technology is introduced. They should be taught progressively, using a small, evolving AI pull-request review workflow where appropriate.

| Order | Topic | Learning objective | Status |
|---|---|---|---|
| F01 | Python workflows | Build sequential and conditional workflows using functions, data structures, loops, and exceptions. | Planned |
| F02 | Testing fundamentals | Test observable behavior, edge cases, and failures with Python `unittest`. | Planned |
| F03 | Workflow limitations | Identify the orchestration problems that arise as a plain Python workflow grows. | Planned |
| F04 | Direct LLM SDK usage | Configure a provider client, send messages, inspect responses, and handle errors. | Planned |
| F05 | LLM integration testing | Test model-dependent code with mocks or deterministic fakes. | Planned |
| F06 | LangChain foundations | Understand chat models, messages, structured outputs, and reusable integrations. | Planned |
| F07 | Why LangGraph? | Explain when explicit stateful orchestration adds value beyond ordinary function calls. | Planned |
| F08 | Observability foundations | Understand traces, debugging, evaluation, and operational evidence. | Planned |
| F09 | Langfuse and LangSmith | Compare capabilities, integrations, deployment options, data handling, and costs. | Planned |

Foundation lessons will receive implementation, Markdown, and test paths when their scope and filenames are established.

## 3. Numbered lesson roadmap

**Default status for every lesson below:** implementation `Planned`; documentation `Planned`; tests `Planned`; learning status `Not assessed`.

File paths are assigned when a lesson is designed. For a practical lesson, the expected pattern is:

- Implementation: `<phase-directory>/<lesson-file>.py`
- Documentation: `<phase-directory>/<lesson-file>.md`
- Dedicated test: `tests/test_<lesson-file>.py`

The implementation, Markdown, test, phase index, and tracker must use consistent names. Do not create empty future lesson files simply to populate the roadmap.

### Phase 01 — Core Graph Model

| Lesson | Topic | Key learning objective |
|---|---|---|
| 05 | State | Define the data a graph needs to read and update. |
| 06 | Nodes | Implement focused units of graph work. |
| 07 | Edges | Connect graph steps and understand execution order. |
| 08 | START / END | Define graph entry and termination. |
| 09 | State updates | Understand how nodes return changes to graph state. |
| 10 | Reducers | Understand how state updates are combined. |

### Phase 02 — Messages and LLM State

| Lesson | Topic | Key learning objective |
|---|---|---|
| 11 | Messages | Understand messages as structured model input and output. |
| 12 | MessagesState | Use a message-oriented graph state. |
| 13 | Message reducers | Understand how message updates are applied. |
| 14 | Message types | Distinguish HumanMessage, AIMessage, ToolMessage, and SystemMessage. |
| 15 | Message history | Track conversation history and its implications. |

### Phase 03 — Control Flow

| Lesson | Topic | Key learning objective |
|---|---|---|
| 16 | Conditional edges | Select the next step based on state or a decision. |
| 17 | Routing | Separate decision logic from execution logic. |
| 18 | Loops | Build bounded iterative workflows. |
| 19 | Recursion limits | Control graph execution and prevent runaway loops. |
| 20 | Command | Combine state updates with control-flow decisions where appropriate. |
| 21 | Send | Dynamically dispatch work to graph nodes. |
| 22 | Map-reduce / fan-out / fan-in | Distribute work and aggregate results. |

### Phase 04 — Persistence and Execution

| Lesson | Topic | Key learning objective |
|---|---|---|
| 23 | Checkpointers | Persist graph execution state. |
| 24 | Threads | Associate checkpoints with a logical execution thread. |
| 25 | Persistence model | Understand what is persisted and how it is organized. |
| 26 | State snapshots | Inspect saved graph states. |
| 27 | Durable execution | Design workflows that can continue across interruptions. |
| 28 | Fault recovery | Recover from failures without corrupting workflow state. |
| 29 | Retry semantics | Understand retry boundaries and repeated side effects. |
| 30 | Time travel / replay | Inspect prior states and replay execution where supported. |

### Phase 05 — Memory

| Lesson | Topic | Key learning objective |
|---|---|---|
| 31 | Short-term memory | Manage information within a conversation or thread. |
| 32 | Long-term memory | Store information across separate interactions. |
| 33 | Threads vs memory | Distinguish execution identity from stored knowledge. |
| 34 | Memory stores | Understand APIs and storage for persistent memory. |
| 35 | Memory design patterns | Choose memory strategies based on the application. |

### Phase 06 — Streaming

| Lesson | Topic | Key learning objective |
|---|---|---|
| 36 | Streaming | Understand incremental output from a running workflow. |
| 37 | Stream modes | Compare supported streaming modes. |
| 38 | State streaming | Observe graph state as execution progresses. |
| 39 | Message streaming | Consume incremental model messages. |
| 40 | Custom streaming | Emit application-specific progress information. |
| 41 | Streaming events | Understand event lifecycles and relevant execution details. |

### Phase 07 — Human-in-the-Loop

| Lesson | Topic | Key learning objective |
|---|---|---|
| 42 | Interrupts | Pause execution at an intentional boundary. |
| 43 | Human-in-the-loop | Incorporate human decisions into workflows. |
| 44 | Inspect state | Examine paused or persisted graph state. |
| 45 | Modify state | Apply controlled state updates. |
| 46 | Resume execution | Continue a paused workflow safely. |

### Phase 08 — Subgraphs and Architecture

| Lesson | Topic | Key learning objective |
|---|---|---|
| 47 | Subgraphs | Compose smaller graphs into larger workflows. |
| 48 | Parent graph | Coordinate high-level workflow responsibilities. |
| 49 | Child graph | Encapsulate domain-specific execution logic. |
| 50 | State boundaries | Define which data crosses graph boundaries. |
| 51 | Subgraph communication | Exchange inputs, outputs, and shared state deliberately. |
| 52 | Multi-stage architecture | Design a workflow with clear component responsibilities. |

### Phase 09 — Runtime and Context

| Lesson | Topic | Key learning objective |
|---|---|---|
| 53 | Runtime | Understand the execution facilities available to graph logic. |
| 54 | Context | Separate run-specific dependencies from graph state. |
| 55 | Runtime configuration | Supply execution options and configurable values. |
| 56 | Dependency/context passing | Pass dependencies without hard-coding infrastructure. |
| 57 | Execution metadata | Understand execution identifiers and metadata. |
| 58 | Store | Understand persistent cross-interaction storage interfaces. |

### Phase 10 — Tools and Agents

| Lesson | Topic | Key learning objective |
|---|---|---|
| 59 | Tools | Define capabilities that model-driven workflows can invoke. |
| 60 | Tool calling | Understand model requests to invoke tools. |
| 61 | Tool execution | Validate, execute, and report tool results. |
| 62 | Tool nodes | Integrate tool execution into a graph. |
| 63 | Agent state | Model the state needed for an agent loop. |
| 64 | Agent loops | Build bounded model-and-tool execution cycles. |
| 65 | Model decisions | Understand how model outputs influence routing and actions. |
| 66 | Agent middleware | Inspect and customize supported execution hooks. |
| 67 | Agent customization | Adapt agent behavior to application requirements. |

### Phase 11 — Multi-Agent Systems

| Lesson | Topic | Key learning objective |
|---|---|---|
| 68 | Multi-agent architectures | Evaluate when multiple agents are justified. |
| 69 | Agent state design | Design state ownership and communication contracts. |
| 70 | Supervisor pattern | Coordinate specialist workers through a supervisor. |
| 71 | Handoff pattern | Transfer control between agents. |
| 72 | Network pattern | Understand agent-to-agent routing. |
| 73 | Hierarchical agents | Organize delegation across multiple levels. |
| 74 | Agent collaboration | Aggregate results and handle coordination failures. |

### Phase 12 — Production Engineering

| Lesson | Topic | Key learning objective |
|---|---|---|
| 75 | Deployment | Package and deploy an AI workflow. |
| 76 | Scaling | Understand capacity, concurrency, and bottlenecks. |
| 77 | Background execution | Run long-running work outside request lifetimes where appropriate. |
| 78 | Authentication | Verify identity and protect application entry points. |
| 79 | Reliability | Design for partial failure and degraded operation. |
| 80 | Error handling | Represent and handle application failures deliberately. |
| 81 | Retries | Apply bounded retries, backoff, and timeouts. |
| 82 | Idempotency | Prevent duplicate requests or side effects from causing incorrect results. |
| 83 | Observability | Connect logs, traces, metrics, and operational diagnosis. |
| 84 | LangSmith | Understand LangSmith capabilities and integration options. |
| 85 | Testing | Test workflows, integrations, failure modes, and regressions. |
| 86 | Production architecture | Make and defend end-to-end architecture decisions. |

### Phase 13 — Langfuse Observability

This phase will be expanded into individually numbered lessons when its implementation begins.

| Topic | Key learning objective | Status |
|---|---|---|
| Traces and observations | Understand tracing concepts and execution structure. | Planned |
| LangGraph integration | Trace graph execution using supported integration patterns. | Planned |
| Prompt management | Manage and evaluate prompts where appropriate. | Planned |
| Evaluation and datasets | Evaluate outputs using repeatable datasets and criteria. | Planned |
| Latency, cost, and errors | Investigate performance and operational failures using available evidence. | Planned |
| Privacy and production operations | Prevent sensitive data leakage and configure tracing responsibly. | Planned |

## 4. PostgreSQL and persistence learning policy

PostgreSQL is introduced when the curriculum needs durable storage or production data management.

The course will distinguish:

- Graph checkpoints used to persist workflow execution state.
- Application records such as tenants, executions, findings, and audit events.
- Conversation threads and longer-lived memory.
- Observability traces and evaluation data.

These are related but distinct concerns. Lessons will explain their boundaries, transaction requirements, concurrency behavior, retention, and recovery implications. The initial Python workflow lessons will not require a running PostgreSQL server.

## 5. Required lesson metadata

Before implementing a lesson, add a detailed entry containing:

- Lesson ID, title, and phase.
- Prerequisites, with links to prerequisite lessons.
- Learning objectives and the engineering problem being solved.
- Implementation path.
- Markdown path.
- Dedicated test path.
- Implementation status.
- Test status.
- Documentation status.
- Learning status.
- Completion and mastery criteria.

Use the following template when a lesson is ready to be designed:

| Field | Value |
|---|---|
| Lesson | To be assigned |
| Phase | To be assigned |
| Prerequisites | To be defined |
| Learning objectives | To be defined |
| Implementation path | To be assigned |
| Markdown path | To be assigned |
| Test path | To be assigned |
| Implementation status | Planned |
| Test status | Planned |
| Documentation status | Planned |
| Learning status | Not assessed |
| Completion criteria | To be defined |
| Mastery criteria | To be defined |

Do not assign fictitious paths or mark missing files as implemented.

## 6. Verification criteria

A practical lesson is `Verified` only when:

1. The Python implementation runs from the documented working directory.
2. The Markdown explanation matches the actual implementation and APIs.
3. The dedicated test passes.
4. Relevant positive, negative, boundary, and error cases are tested where appropriate.
5. Commands and expected behavior are checked.
6. The phase README links to the lesson.
7. This tracker accurately reflects the lesson's state.
8. Default tests do not require real API credentials, paid API calls, or network availability.

Framework-specific APIs must be checked against current official documentation when the lesson is implemented.

## 7. Mastery criteria

A lesson is `Mastered` only when the learner can:

- Explain the concept without merely repeating the lesson.
- Implement a comparable example independently.
- Solve exercises with increasing difficulty.
- Diagnose a deliberate failure.
- Explain important trade-offs and limitations.
- Identify when the concept or abstraction is unnecessary.

Mastery is assessed through demonstrated understanding, not file creation or successful test execution alone.

## 8. Curriculum maintenance

Whenever a lesson changes, review its implementation, Markdown explanation, tests, commands, expected behavior, phase README, and tracker entry.

When a file is renamed or moved, update all references.

Keep future lessons planned until work begins. Update statuses only after inspecting the actual result. Do not create empty placeholders solely to make the directory tree appear complete.