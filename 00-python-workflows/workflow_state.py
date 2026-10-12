
def create_initial_state():
    state = {
        "title": "Fix login validation",
        "description": "Validate user input before login",
        "status": "started",
    }

    return state


def analyze_state(state):
    description = state["description"]

    if len(description) >= 20:
        assessment = "Sufficient description"
    else:
        assessment = "Description needs more detail"

    state["assessment"] = assessment
    state["status"] = "analyzed"

    return state


def generate_summary_state(state):
    title = state["title"]
    assessment = state["assessment"]

    state["summary"] = f"PR Review: {title} - {assessment}"
    state["status"] = "completed"

    return state


def run_workflow():
    state = create_initial_state()
    analyze_state(state)
    generate_summary_state(state)

    return state


def main():
    state = run_workflow()
    print(state)


if __name__ == "__main__":
    main()
