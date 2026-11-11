# Bug reports for exercise3.py

Line: 3
Problem: The docstring says an empty list has average 0, but dividing by len(numbers) on an empty list causes a ZeroDivisionError. The function should handle empty lists by returning 0 without raising an exception.
Example: average([]) raises ZeroDivisionError, expected 0.
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8
Problem: The docstring says "The first word of the text, or "" if the text is empty", but text.split()[0] on an empty string (or empty list after split) raises an IndexError. It should return "" for empty input.
Example: first_word("") returns IndexError, expected "".
Fix: return text.split()[0] if text.strip() else ""

Line: 12
Problem: The docstring says "If total is 0, the result is 0", but the current code returns a division by zero error. The function must return 0 when total is 0 to avoid division by zero.
Example: percent(5, 0) raises ZeroDivisionError, expected 0.
Fix: return part / total * 100 if total != 0 else 0
