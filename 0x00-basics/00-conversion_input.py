#!/usr/bin/env python3
"""
type conversion
"""
from datetime import date
from datetime import datetime

def age(birthday):
    """
    calculates the current age
    """
    today = datetime.today()
    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1
    print("{} years old".format(age))

birthday = input('What is your birthday? (\"yyyy-m-d") ')
birthdayTime = datetime.strptime(birthday, '%Y-%m-%d')

age(birthday=birthdayTime)
