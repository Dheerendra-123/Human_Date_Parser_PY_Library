# human_date_parser_ai/parser.py

import datetime
import re
import spacy
import dateparser
from dateparser.search import search_dates
import holidays
from typing import Optional

nlp = spacy.load("en_core_web_sm")

# Define replacements for common vague terms
FUZZY_REPLACEMENTS = {
    "tmrw": "tomorrow",
    "2day": "today",
    "couple of days": "2 days",
    "fortnight": "14 days",
    "next weekend": "next Saturday",
    "this weekend": "this Saturday",
    "mid next week": "next Wednesday"
}

INDIAN_HOLIDAYS = holidays.India()


def normalize_text(text: str) -> str:
    text = text.lower().strip()
    for fuzzy, replacement in FUZZY_REPLACEMENTS.items():
        pattern = r'\\b' + re.escape(fuzzy) + r'\\b'
        text = re.sub(pattern, replacement, text)
    return text


def resolve_holiday_reference(text: str, base_date: datetime.datetime) -> Optional[str]:
    for name, date in INDIAN_HOLIDAYS.items():
        if name.lower() in text:
            if "after" in text:
                return (date + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            elif "before" in text:
                return (date - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            else:
                return date.strftime("%Y-%m-%d")
    return None


def parse(text: str, *, debug=False, fallback_now=True) -> Optional[datetime.datetime]:
    if not text or not isinstance(text, str):
        return datetime.datetime.now() if fallback_now else None

    original = text
    text = normalize_text(text)
    base_date = datetime.datetime.now()

    # Determine direction preference
    if any(kw in text for kw in ["ago", "last", "previous", "yesterday"]):
        prefer = 'past'
    else:
        prefer = 'future'

    # Handle holiday references
    holiday_resolved = resolve_holiday_reference(text, base_date)
    if holiday_resolved:
        # Replace holiday name with resolved date
        text = re.sub(r'after .*', f'in 1 day after {holiday_resolved}', text)
        text = re.sub(r'before .*', f'1 day before {holiday_resolved}', text)
        if debug:
            print(f"[DEBUG] Holiday resolved text: {text}")

    settings = {
        'PREFER_DATES_FROM': prefer,
        'RETURN_AS_TIMEZONE_AWARE': False,
        'RELATIVE_BASE': base_date,
        'STRICT_PARSING': False,
    }

    # First pass
    result = dateparser.parse(text, settings=settings)
    if debug:
        print(f"[DEBUG] Input: '{original}' → Normalized: '{text}' → Parsed: {result}")

    # Fallback search_dates
    if result is None:
        found = search_dates(text, settings=settings)
        if found:
            result = found[0][1]
            if debug:
                print(f"[DEBUG] Fallback search_dates(): {found}")

    return result or (base_date if fallback_now else None)


# Example usage
if __name__ == "__main__":
    test_cases = [
        "tmrw",
        "2 weeks after Diwali",
        "mid next week",
        "last Monday",
        "2 weeks ago",
        "just before Christmas",
        "in a couple of days",
    ]

    for phrase in test_cases:
        dt = parse(phrase, debug=True)
        print(f"'{phrase}' → {dt}")
