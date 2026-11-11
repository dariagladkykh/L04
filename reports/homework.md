# Bug reports for homework.py

Line: 3
Problem: The docstring says the formula is "c * 9 / 5 + 32", but the code uses "c * 5 / 9 + 32", which is incorrect. The correct conversion from Celsius to Fahrenheit is F = C * 9/5 + 32, not C * 5/9 + 32.
Example: celsius_to_fahrenheit(0) returns 32, expected 32 (this is correct by coincidence), but celsius_to_fahrenheit(100) returns 212, expected 212 — wait, actually 100 * 5 / 9 + 32 ≈ 100, not 212. So it's wrong: celsius_to_fahrenheit(100) returns 53.888..., expected 212.
Fix: return c * 9 / 5 + 32

Line: 8
Problem: The docstring says "divisible by 4, except years divisible by 100, unless they are also divisible by 400", which means a year is a leap year if: divisible by 4 and (not divisible by 100 or divisible by 400). The current code returns True when year % 4 == 0 and year % 100 != 0, which incorrectly excludes years divisible by 400 (like 2000). For example, 2000 should be a leap year but is excluded.
Example: is_leap_year(2000) returns False, expected True.
Fix: return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

Line: 20
Problem: The docstring says "Second largest distinct value... or None if there are fewer than 2 distinct values". The current code returns None if there are fewer than 1 distinct values (i.e., empty list or all same values), but it should return None only when there are fewer than 2 distinct values. For a list with one distinct value (e.g., [5,5,5]), there is only one distinct value, so second largest should be None. However, if the list is empty, set(numbers) is empty, so len(values) is 0, and the condition len(values) < 1 returns True, so it returns None — which is correct. But if the list has one distinct value, len(values) is 1, so len(values) < 1 is False, and it returns values[1], which causes an index error. For example, [5] → set([5]) → sorted(set(...), reverse=True) = [5], len(values)=1 → values[1] raises IndexError.
Example: second_largest([5]) returns IndexError, expected None.
Fix: return values[1] if len(values) >= 2 else None
