def celsius_to_fahrenheit(c):
    """Temperature in Fahrenheit: c * 9 / 5 + 32"""
    return c * 9 / 5 + 32


def is_leap_year(year):
    """True if year is a leap year: divisible by 4, except years divisible by 100, unless they are also divisible by 400"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def count_vowels(text):
    """Number of vowels (a, e, i, o, u) in the text, uppercase or lowercase"""
    return sum(1 for c in text if c in "aeiou")


def second_largest(numbers):
    """Second largest distinct value in the list, or None if there are fewer than 2 distinct values"""
    values = sorted(set(numbers), reverse=True)
    if len(values) < 1:
        return None
    return values[1]


def binary_search(items, target):
    """Index of target in the sorted list items, or -1 if it is not there"""
    low, high = 0, len(items) - 1
    while low < high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
