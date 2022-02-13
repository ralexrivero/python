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
    today = date.today()
    age = today.year - birthday.year
    print(age)

birthday = input('What is your birthday? (\"yyyy-m-d") ')
birthdayTime = datetime.strptime(birthday, '%Y-%m-%d')
print(type(birthdayTime))

age(birthday=birthdayTime)
