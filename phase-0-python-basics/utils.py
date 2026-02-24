# utils.py

def section(title: str):
    """Print formatted section header"""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def safe_int_input(prompt: str):
    """Safely convert user input to integer"""
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid number entered.")
        return None
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return None