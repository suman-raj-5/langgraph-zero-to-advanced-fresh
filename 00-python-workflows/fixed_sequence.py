
def collect_pr_details():
    print("Step 1: Collecting pull request details")
    return "Fix login validation"


def analyze_pr(title):
    print("Step 2: Analyzing pull request")
    return f"Security issue found in: {title}"


def choose_review_action(analysis):
    if "security issue" in analysis.lower():
        return "security_warning"

    return "normal_summary"


def generate_summary(analysis):
    print("Step 3: Generating review summary")
    return f"Review summary: {analysis}"


def run_workflow():
    title = collect_pr_details()
    analysis = analyze_pr(title)

    action = choose_review_action(analysis)

    if action == "security_warning":
        summary = f"Security warning: {analysis}"
    else:
        summary = generate_summary(analysis)

    return summary


def main():
    result = run_workflow()
    print(result)


if __name__ == "__main__":
    main()
