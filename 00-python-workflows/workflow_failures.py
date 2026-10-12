security_check_attempts = 0


def collect_pr_details():
    print("Step 1: Collecting pull request details")
    return "Fix login validation"


def analyze_pr(title):
    print("Step 2: Analyzing pull request")
    return f"Analysis complete for: {title}"


def run_security_check():
    global security_check_attempts
    security_check_attempts += 1

    print(f"Step 3: Security check attempt {security_check_attempts}")

    if security_check_attempts == 1:
        raise RuntimeError("Security service is temporarily unavailable")

    print("Security check passed")


def generate_summary(analysis):
    print("Step 4: Generating review summary")
    return f"Review summary: {analysis}"


def run_workflow():
    title = collect_pr_details()
    analysis = analyze_pr(title)

    security_check_passed = False

    for attempt in range(2):
        try:
            run_security_check()
            security_check_passed = True
            break
        except RuntimeError as error:
            print(f"Security check failed: {error}")

            if attempt == 0:
                print("Retrying security check...")

    if not security_check_passed:
        print("Workflow stopped: security check could not be completed")
        return

    summary = generate_summary(analysis)
    print(summary)


def main():
    run_workflow()


if __name__ == "__main__":
    main()
