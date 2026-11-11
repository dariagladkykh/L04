# Bug reports for exercise1.py

Line: 3
Problem: is_even checks if n % 2 == 1, which is true for odd numbers, but the docstring says "true for even numbers". It should check for evenness using n % 2 == 0.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: rectangle_area returns the sum of width and height, but the docstring says "area of a rectangle", which should be width multiplied by height.
Example: rectangle_area(5, 3) returns 8, expected 15.
Fix: return width * height

Line: 12
Problem: double returns n + 2, but the docstring says "twice the number n", which means n * 2.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
