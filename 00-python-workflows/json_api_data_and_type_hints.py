
import json


def parse_pr_payload(payload: str) -> dict[str, object]:
    """Parse JSON text and validate a PR API payload."""
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ValueError("Payload must contain valid JSON") from exc

    if not isinstance(data, dict):
        raise ValueError("PR payload must be a JSON object")

    number = data.get("number")
    title = data.get("title")
    changed_files = data.get("changed_files")

    if type(number) is not int or number <= 0:
        raise ValueError("PR number must be a positive integer")

    if not isinstance(title, str) or not title.strip():
        raise ValueError("PR title must be a non-empty string")

    if type(changed_files) is not int or changed_files < 0:
        raise ValueError("changed_files must be a non-negative integer")

    return {
        "number": number,
        "title": title.strip(),
        "changed_files": changed_files,
    }


def serialize_pr_payload(pr_details: dict[str, object]) -> str:
    """Serialize validated PR data to JSON text."""
    return json.dumps(pr_details)


def main() -> None:
    payload = (
        '{"number": 42, "title": "Fix login validation", '
        '"changed_files": 3}'
    )

    pr_details = parse_pr_payload(payload)
    print("Parsed PR:", pr_details)

    serialized = serialize_pr_payload(pr_details)
    print("JSON output:", serialized)


if __name__ == "__main__":
    main()
