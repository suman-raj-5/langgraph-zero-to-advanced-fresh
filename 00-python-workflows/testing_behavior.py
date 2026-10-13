
def run_security_check():
    """Simulate a security-check dependency."""
    return True


def generate_summary(analysis):
    """Generate a summary from the analysis."""
    return f"Review summary: {analysis}"


def run_workflow():
    """Run the review workflow using its dependencies."""
    analysis = "Analysis complete for: Fix login validation"

    if not run_security_check():
        return None

    return generate_summary(analysis)


if __name__ == "__main__":
    print(run_workflow())
