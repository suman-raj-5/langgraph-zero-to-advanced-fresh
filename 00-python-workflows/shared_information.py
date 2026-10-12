
def collect_pr_details():
    pr_details = {
        "title": "Fix login validation",
        "description": "Validate empty usernames and reject invalid login requests.",
        "changed_files": "auth.py, login.py",
        "test_status": "passed",
        "security_findings": "SQL injection risk",
    }

    return pr_details


def generate_summary(pr_details):
    print(f"PR: {pr_details['title']}")
    print(f"Changed files: {pr_details['changed_files']}")
    print(f"Tests: {pr_details['test_status']}")
    print(f"Security findings: {pr_details['security_findings']}")


def run_workflow():
    pr_details = collect_pr_details()
    generate_summary(pr_details)


def main():
    run_workflow()


if __name__ == "__main__":
    main()
