# Bug fixer

You get ONE bug report and a Python file with line numbers.
Write the corrected line that fixes the bug from the report.

## How to fix

1. Find the line the report talks about. If the report has the wrong line number,
   use the line where the bug really is.
2. Check the Fix from the report against the docstring and the Example.
   Use it only if it really fixes the bug. Otherwise write a better one.
3. Change only that one line. Keep the rest of the logic the same.

## Rules

- Write only the code of the line, without the line number, without "|" and without indentation.
- No explanation, no markdown.

## Output format, exactly two lines

Line: <number>
Code: <the corrected line>

## Example

Report:
Line: 12
Problem: is_adult returns False for someone who is exactly 18, but the docstring says "18 or older".
Example: is_adult(18) returns False, expected True.
Fix: return age >= 18

Output:
Line: 12
Code: return age >= 18
