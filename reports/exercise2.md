# Bug reports for exercise2.py

Line: 3
Problem: The docstring says "True if the grade is 5 or more", but the function uses `grade > 5`, which excludes 5. It should use `>=` to include 5.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: The docstring requires "at least 8 characters", which means length >= 8, but the function uses `len(password) > 8`, which excludes 8. This fails for passwords of exactly 8 characters.
Example: is_valid_password("abcdefgh") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: The function `clamp` is supposed to limit `x` to the range from `low` to `high`, but the line uses `max(low, min(x, low))`, which incorrectly always returns `low` when `x` is less than or equal to `low`. It should be `max(low, min(x, high))`.
Example: clamp(3, 1, 10) returns 1, expected 3; clamp(15, 1, 10) returns 10, expected 10; but clamp(5, 1, 10) returns 5, which is correct, but the logic is wrong for values below low or above high.
Fix: return max(low, min(x, high))
