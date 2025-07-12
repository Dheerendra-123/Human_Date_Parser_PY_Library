from datetime import datetime
import dateparser


def parse(text: str, settings: dict = None, *, fallback_now=False, debug=False) -> datetime:
    """
    Convert a natural language date string into a datetime object.

    Parameters:
    - text (str): A human-readable date string like "tomorrow", "next Friday", etc.
    - settings (dict): Optional dictionary to override default dateparser settings.
    - fallback_now (bool): If True, return current datetime when parsing fails.
    - debug (bool): If True, print debug info.

    Returns:
    - datetime object if successful, else None or current datetime
    """
    if not isinstance(text, str) or not text.strip():
        if debug:
            print("[DEBUG] Invalid input.")
        return datetime.now() if fallback_now else None

    text = text.strip()

    default_settings = {
        'PREFER_DATES_FROM': 'future',
        'RELATIVE_BASE': datetime.now(),
        'RETURN_AS_TIMEZONE_AWARE': False,
        'PARSERS': ['relative-time', 'absolute-time', 'custom-formats'],
        'STRICT_PARSING': False,
    }

    if settings:
        default_settings.update(settings)

    if debug:
        print(f"[DEBUG] Parsing: '{text}' with settings: {default_settings}")

    result = dateparser.parse(text, settings=default_settings)

    if debug and result is None:
        print("[DEBUG] Parsing failed.")

    return result or (datetime.now() if fallback_now else None)
