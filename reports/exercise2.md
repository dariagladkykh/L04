# Bug reports for exercise2.py

Line: 3
Problem: is_passing uses `>` instead of `>=` for the condition, but the docstring says "5 or more", which means it should include 5.
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: is_valid_password uses `len(password) > 8` instead of `>= 8`, but the docstring says "At least 8 characters", which means 8 or more.
Example: is_valid_password("abcdefgh") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12
Problem: clamp uses `max(low, min(x, low))`, which simplifies to `low`, making it always return low regardless of x. It should return `max(low, min(x, high))` to properly clamp between low and high.
Example: clamp(10, 1, 5) returns 1, expected 5.
Fix: return max(low, min(x, high))
