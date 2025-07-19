# human-date-parser

A lightweight and intuitive Python library designed to effortlessly convert natural language date expressions into precise Python datetime objects. Simplify date parsing in your applications by understanding human-friendly inputs like "today," "next Monday," or "in 3 days."

## Features

- **Effortless Parsing**: Convert common natural language date phrases into datetime objects.
- **Relative Date Handling**: Accurately interpret "today," "tomorrow," "yesterday," and relative terms like "in X days/weeks/months/years" or "X days/weeks/months/years ago."
- **Weekday Recognition**: Understand "next Monday," "last Friday," and similar weekday references.
- **Complex Expressions**: Handle combinations like "in 2 weeks and 3 days."
- **Robust Error Handling**: Returns None for unparsable input, allowing for graceful error management.

## Installation

You can install human-date-parser directly from your terminal:

```bash
pip install human-date-parser
```

If you are developing the library locally, you can install it in editable mode:

```bash
pip install -e .
```

## Usage

The primary function of the library is `parse()`, which takes a string representing a natural language date and returns a `datetime.datetime` object. All parsed dates will have their time components set to 00:00:00 (midnight) unless specified otherwise in the natural language input (though this library primarily focuses on date parsing, not time).

## Code Examples

Let's explore how to use `parse()` with various natural language inputs.

```python
from human_date_parser import parse
import datetime

# For consistent examples, we'll assume the current date is July 12, 2025.
# In a real application, parse_date will use the actual current date.
```

### 📅 Basic Dates

Easily parse common, absolute date references.

```python
print(parse("today"))        # -> datetime.datetime(2025, 7, 12, 0, 0)
print(parse("tomorrow"))     # -> datetime.datetime(2025, 7, 13, 0, 0)
print(parse("yesterday"))    # -> datetime.datetime(2025, 7, 11, 0, 0)
```

### ⏳ Relative Future

Calculate dates relative to the current day, looking forward.

```python
print(parse("in 3 days"))     # -> datetime.datetime(2025, 7, 15, 0, 0)
print(parse("in 1 week"))     # -> datetime.datetime(2025, 7, 19, 0, 0)
print(parse("in 2 months"))   # -> datetime.datetime(2025, 9, 12, 0, 0)
```

### ⌛ Relative Past

Calculate dates relative to the current day, looking backward.

```python
print(parse("2 days ago"))    # -> datetime.datetime(2025, 7, 10, 0, 0)
print(parse("3 weeks ago"))   # -> datetime.datetime(2025, 6, 21, 0, 0)
print(parse("1 year ago"))    # -> datetime.datetime(2024, 7, 12, 0, 0)
```

### 🗓️ Weekdays

Determine the date of the next or last occurrence of a specific weekday.

```python
print(parse("next Monday"))   # → Next upcoming Monday (e.g., datetime.datetime(2025, 7, 14, 0, 0))
print(parse("last Friday"))   # → Previous Friday (e.g., datetime.datetime(2025, 7, 11, 0, 0))
```

### 🧠 Complex Natural Language

The parser can combine multiple relative terms for more nuanced date calculations.

```python
print(parse("in 2 weeks and 3 days"))   # → Adds both weeks and days (e.g., datetime.datetime(2025, 7, 29, 0, 0))
print(parse("next year"))               # → Approx. one year ahead (e.g., datetime.datetime(2026, 7, 12, 0, 0))
print(parse("last month"))              # → One month before today (e.g., datetime.datetime(2025, 6, 12, 0, 0))
```

### ⚠️ Invalid Input Handling

For inputs that cannot be parsed into a valid date, the function gracefully returns None.

```python
result = parse("not a date")
if result is None:
    print("Could not parse date.")
# Output: Could not parse date.
```

### 🧪 Example in Real Use

Here's a practical example of how you might use human-date-parser to set a reminder.

```python
# Schedule a reminder 5 days from now
reminder_date = parse("in 5 days")

if reminder_date:
    print("Reminder set for:", reminder_date.strftime("%Y-%m-%d"))
# Output (assuming today is July 12, 2025): Reminder set for: 2025-07-17
else:
    print("Failed to set reminder. Please check the date input.")
```

## Contributing

Contributions are welcome! If you have suggestions for new features, improvements, or bug fixes, please open an issue or submit a pull request on the project's GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.