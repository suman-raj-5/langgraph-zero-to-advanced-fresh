
def collect_pr_details():
    pr_details = {
        "title": "Fix login validation",
        "description": "Validate user input before login",
    }

    return pr_details


def analyze_pr(pr_details):
    title = pr_details["title"]
    description = pr_details["description"]

    if len(description) >= 20:
        assessment = "Sufficient description"
    else:
        assessment = "Description needs more detail"

    analysis = {
        "title": title,
        "assessment": assessment,
    }

    return analysis


def generate_summary(analysis):
    title = analysis["title"]
    assessment = analysis["assessment"]

    summary = f"PR Review: {title} - {assessment}"

    return summary


def run_workflow():
    pr_details = collect_pr_details()
    analysis = analyze_pr(pr_details)
    summary = generate_summary(analysis)

    return summary


def main():
    summary = run_workflow()
    print(summary)


if __name__ == "__main__":
    main()
