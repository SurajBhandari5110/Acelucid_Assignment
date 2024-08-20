import re
import datetime

def find_valid_date(string):
    date_pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')
    match = date_pattern.search(string)

    if match:
        mm, dd, yyyy = match.groups()
        try:
            datetime.datetime(int(yyyy), int(mm), int(dd))
            return f"{mm}{dd}{yyyy}"
        except ValueError:
            return None  # Invalid date

    return None  # No date found

text = "This is a string with a date 08202024 in it."
valid_date = find_valid_date(text)

if valid_date:
    print("Valid date found:", valid_date)
else:
    print("No valid date found.")