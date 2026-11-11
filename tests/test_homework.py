import os
import sqlite3
import subprocess

import pytest

import homework
from homework import *


# bug report 1
def test_r1_celsius_to_fahrenheit_correct_formula():
    assert celsius_to_fahrenheit(100) == pytest.approx(212, rel=1e-3)


# bug report 2
def test_r2_is_leap_year_2000():
    assert is_leap_year(2000) == True


# bug report 3
def test_r3_second_largest_one_distinct_value():
    assert second_largest([5]) == None
