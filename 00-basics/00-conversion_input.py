#!/usr/bin/env python3
"""
type conversion
"""
from datetime import date


def age(birthday):
    """
    calculates the current age
    """
    today = date.today()
    age = today.year - birthday.year
    print(age)

ask = input('What is your birthday? (\"yyyy,m,d/") ')
print(type(date(ask)))

birthday = date(1980,9,24)

age(birthday=birthday)
