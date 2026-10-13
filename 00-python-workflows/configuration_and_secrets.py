
import os


def load_config():
    """Load and validate application configuration."""
    model_name = os.getenv("MODEL_NAME")
    max_retries_value = os.getenv("MAX_RETRIES", "2")

    if not model_name or not model_name.strip():
        raise ValueError("MODEL_NAME must be set and non-empty")

    try:
        max_retries = int(max_retries_value)
    except (TypeError, ValueError) as exc:
        raise ValueError("MAX_RETRIES must be an integer") from exc

    if max_retries < 0:
        raise ValueError("MAX_RETRIES must be non-negative")

    return {
        "model_name": model_name.strip(),
        "max_retries": max_retries,
    }


def main():
    config = load_config()
    print(f"Model: {config['model_name']}")
    print(f"Maximum retries: {config['max_retries']}")


if __name__ == "__main__":
    main()
