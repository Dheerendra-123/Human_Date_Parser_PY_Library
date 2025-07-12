from datetime import datetime
import dateparser
from dateparser.search import search_dates


def parse(text: str, settings: dict = None, *, fallback_now=False, debug=False) -> datetime:
    """
    Parse human-readable date strings into datetime objects.

    Parameters:
        text (str): The natural language date input.
        settings (dict): Optional dateparser settings.
        fallback_now (bool): Return datetime.now() if parsing fails.
        debug (bool): Print debug info.

    Returns:
        datetime or None
    """
    if not isinstance(text, str) or not text.strip():
        if debug:
            print("[DEBUG] Invalid input")
        return datetime.now() if fallback_now else None

    text = text.strip()

    default_settings = {
        'PREFER_DATES_FROM': 'future',
        'RETURN_AS_TIMEZONE_AWARE': False,
        'RELATIVE_BASE': datetime.now(),
        'STRICT_PARSING': False,
    }

    if settings:
        default_settings.update(settings)

    if debug:
        print(f"[DEBUG] Parsing: '{text}' with settings: {default_settings}")

    result = dateparser.parse(text, settings=default_settings)

    # Fallback: Try fuzzy match using search_dates
    if result is None:
        search_result = search_dates(text, settings=default_settings)
        if search_result:
            if debug:
                print(f"[DEBUG] Fallback search_dates() success: {search_result}")
            result = search_result[0][1]

    if debug and result is None:
        print(f"[DEBUG] Failed to parse: '{text}'")

    return result or (datetime.now() if fallback_now else None)
