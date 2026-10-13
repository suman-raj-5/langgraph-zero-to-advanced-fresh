
def create_review_state(title, findings=None):
    """Create review state with an independent findings list."""
    if findings is None:
        findings = []

    return {
        "title": title,
        "findings": findings,
        "status": "started",
    }


def add_finding(state, finding):
    """Add a finding to this review's state."""
    state["findings"].append(finding)
    state["status"] = "analyzed"
    return state


def run_review(title, finding=None):
    """Run one review with its own state."""
    state = create_review_state(title)

    if finding is not None:
        add_finding(state, finding)

    return state


def main():
    review_a = run_review(
        "Authentication fix",
        "Hardcoded secret detected",
    )
    review_b = run_review("Documentation update")

    print("PR A:", review_a)
    print("PR B:", review_b)
    print(
        "Same findings list:",
        review_a["findings"] is review_b["findings"],
    )


if __name__ == "__main__":
    main()
