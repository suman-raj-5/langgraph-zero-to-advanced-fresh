
def collect_pr_details():
    title = "Fix login validation"
    description = "Validate empty usernames and reject invalid login requests."

    return title, description


def analyze_pr(description):
    description_length = len(description)

    if description_length < 30:
        return "The PR description needs more detail."

    return "The PR description has enough detail."


def generate_summary(title, review):
    return f"Pull request: {title}\nReview: {review}"


def run_workflow():
    title, description = collect_pr_details()
    review = analyze_pr(description)
    summary = generate_summary(title, review)

    return summary


def main():
    result = run_workflow()
    print(result)


if __name__ == "__main__":
    main()
