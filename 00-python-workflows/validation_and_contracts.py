
def validate_pr_details(pr_details):
    """Validate the required fields for an AI PR review."""
    if not isinstance(pr_details, dict):
        raise ValueError("PR details must be a dictionary")

    title = pr_details.get("title")
    description = pr_details.get("description")

    if not isinstance(title, str) or not title.strip():
        raise ValueError("PR title must be a non-empty string")

    if not isinstance(description, str) or not description.strip():
        raise ValueError("PR description must be a non-empty string")

    return pr_details


def analyze_pr(pr_details):
    """Analyze PR details only after validating the input."""
    validate_pr_details(pr_details)

    if len(pr_details["description"]) >= 20:
        assessment = "Sufficient description"
    else:
        assessment = "Description needs more detail"

    return {
        "title": pr_details["title"],
        "assessment": assessment,
    }


def main():
    pr_details = {
        "title": "Fix login validation",
        "description": "Validate user input before login",
    }

    result = analyze_pr(pr_details)
    print("PR analysis:", result)


if __name__ == "__main__":
    main()
