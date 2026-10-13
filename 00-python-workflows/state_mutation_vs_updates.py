
def create_initial_state():
    """Create the initial state for an AI PR review."""
    return {
        "title": "Fix authentication",
        "description": "Validate login input",
        "status": "started",
    }


# Approach 1: Modify the shared dictionary directly.
def analyze_with_mutation(state):
    """Analyze the PR by modifying the original state."""
    state["assessment"] = "Sufficient description"
    state["status"] = "analyzed"
    return state


# Approach 2: Return an update without modifying the original state.
def analyze_with_updates(state):
    """Return analysis results without changing the input state."""
    return {
        "assessment": "Sufficient description",
        "status": "analyzed",
    }


def run_mutation_workflow():
    """Run the workflow using shared dictionary mutation."""
    state = create_initial_state()
    analyze_with_mutation(state)
    return state


def run_update_workflow():
    """Run the workflow by explicitly applying returned updates."""
    state = create_initial_state()
    update = analyze_with_updates(state)
    state.update(update)
    return state


def main():
    mutation_result = run_mutation_workflow()
    update_result = run_update_workflow()

    print("Mutation workflow:", mutation_result)
    print("Update workflow:", update_result)
    print("Equivalent final states:", mutation_result == update_result)


if __name__ == "__main__":
    main()
