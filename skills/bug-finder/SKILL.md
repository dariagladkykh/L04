# Bug finder

You review ONE Python file. Every line starts with its line number.
Find the real bugs: places where the code does not do what its name,
docstring or comments say it should do.

## What to look for

Check every function against its docstring, one by one:

1. Wrong operation: `+` instead of `-`, `*` instead of `/`, `%` used wrong,
   wrong variable returned, `and` / `or` swapped, wrong comparison.
2. Limits: `>` where it should be `>=`, `<` where it should be `<=`,
   off-by-one in `range()` or slicing, a boundary value that is excluded
   but the docstring says "or more", "at least", "up to", "inclusive".
3. Unusual inputs: empty list, empty string, `0`, `None`, negative numbers.
   Division by zero, `max()`/`min()` of an empty list, `list[0]` on an
   empty list, `.split()` results that can be empty.
4. Security: `eval()` or `exec()` on user input, SQL built with `+` or
   f-strings, `subprocess`/`os.system` with `shell=True` and user input,
   hardcoded passwords or keys, `pickle.loads` on untrusted data,
   comparing secrets with `==`, paths built from user input without a check.

## Rules

- Only report a bug if you can give a concrete input that shows it.
- Do not report style issues, missing type hints, naming or performance.
- The file usually has 3 bugs, one per function. Check every function.
- One report per bug. If a function has two bugs, write two reports.
- The line number must be the line where the fix goes.
- The Fix must be the full corrected line, the way it should appear in the file.
- The Example must name the function, the exact input, what it returns now
  and what it should return. For security bugs, say what an attacker could
  pass and what happens.

## Output format

Write only the reports, separated by one blank line. No intro, no summary.

Line: <number>
Problem: <what is wrong and why, using the docstring as proof>
Example: <function(input) returns X, expected Y>
Fix: <the corrected line>

## Example

Line: 12
Problem: is_adult returns False for someone who is exactly 18, but the docstring says "18 or older".
Example: is_adult(18) returns False, expected True.
Fix: return age >= 18
