human-date-parser
A lightweight and intuitive Python library designed to effortlessly convert natural language date expressions into precise Python datetime objects. Simplify date parsing in your applications by understanding human-friendly inputs like "today," "next Monday," or "in 3 days."

Features
Effortless Parsing: Convert common natural language date phrases into datetime objects.

Relative Date Handling: Accurately interpret "today," "tomorrow," "yesterday," and relative terms like "in X days/weeks/months/years" or "X days/weeks/months/years ago."

Weekday Recognition: Understand "next Monday," "last Friday," and similar weekday references.

Complex Expressions: Handle combinations like "in 2 weeks and 3 days."

Robust Error Handling: Returns None for unparsable input, allowing for graceful error management.

Installation
You can install human-date-parser directly from your terminal:

pip install human-date-parser

If you are developing the library locally, you can install it in editable mode:

pip install -e .

Usage
The primary function of the library is parse_date, which takes a string representing a natural language date and returns a datetime.datetime object. All parsed dates will have their time components set to 00:00:00 (midnight) unless specified otherwise in the natural language input (though this library primarily focuses on date parsing, not time).

Code Examples
Let's explore how to use parse_date with various natural language inputs.

from human_date_parser import parse_date
import datetime

# For consistent examples, we'll assume the current date is July 12, 2025.
# In a real application, parse_date will use the actual current date.

📅 Basic Dates
Easily parse common, absolute date references.

print(parse_date("today"))        # -> datetime.datetime(2025, 7, 12, 0, 0)
print(parse_date("tomorrow"))     # -> datetime.datetime(2025, 7, 13, 0, 0)
print(parse_date("yesterday"))    # -> datetime.datetime(2025, 7, 11, 0, 0)

⏳ Relative Future
Calculate dates relative to the current day, looking forward.

print(parse_date("in 3 days"))     # -> datetime.datetime(2025, 7, 15, 0, 0)
print(parse_date("in 1 week"))     # -> datetime.datetime(2025, 7, 19, 0, 0)
print(parse_date("in 2 months"))   # -> datetime.datetime(2025, 9, 12, 0, 0)

⌛ Relative Past
Calculate dates relative to the current day, looking backward.

print(parse_date("2 days ago"))    # -> datetime.datetime(2025, 7, 10, 0, 0)
print(parse_date("3 weeks ago"))   # -> datetime.datetime(2025, 6, 21, 0, 0)
print(parse_date("1 year ago"))    # -> datetime.datetime(2024, 7, 12, 0, 0)

🗓️ Weekdays
Determine the date of the next or last occurrence of a specific weekday.

print(parse_date("next Monday"))   # → Next upcoming Monday (e.g., datetime.datetime(2025, 7, 14, 0, 0))
print(parse_date("last Friday"))   # → Previous Friday (e.g., datetime.datetime(2025, 7, 11, 0, 0))

🧠 Complex Natural Language
The parser can combine multiple relative terms for more nuanced date calculations.

print(parse_date("in 2 weeks and 3 days"))   # → Adds both weeks and days (e.g., datetime.datetime(2025, 7, 29, 0, 0))
print(parse_date("next year"))               # → Approx. one year ahead (e.g., datetime.datetime(2026, 7, 12, 0, 0))
print(parse_date("last month"))              # → One month before today (e.g., datetime.datetime(2025, 6, 12, 0, 0))

⚠️ Invalid Input Handling
For inputs that cannot be parsed into a valid date, the function gracefully returns None.

result = parse_date("not a date")
if result is None:
    print("Could not parse date.")
# Output: Could not parse date.

🧪 Example in Real Use
Here's a practical example of how you might use human-date-parser to set a reminder.

# Schedule a reminder 5 days from now
reminder_date = parse_date("in 5 days")

if reminder_date:
    print("Reminder set for:", reminder_date.strftime("%Y-%m-%d"))
# Output (assuming today is July 12, 2025): Reminder set for: 2025-07-17
else:
    print("Failed to set reminder. Please check the date input.")

Contributing
Contributions are welcome! If you have suggestions for new features, improvements, or bug fixes, please open an issue or submit a pull request on the project's GitHub repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.