# Bug reports for exercise1.py

Line: 3
Problem: The function is_even checks if n % 2 == 1, which is true for odd numbers, but the docstring says it should return true for even numbers.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: The function rectangle_area returns the sum of width and height, but the docstring says it should return the area of a rectangle, which is width times height.
Example: rectangle_area(3, 4) returns 7, expected 12.
Fix: return width * height

Line: 12
Problem: The function double adds 2 to n, but the docstring says it should return twice the number n.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
