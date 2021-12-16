#!/usr/bin/env python3
print("Welcome to the leap year evaluator!")
year = int(input("Which year do you want to check?: "))


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


leap = leap_year(year)
print(f"The year {year} is {leap} year")

days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print("Days in a month")


def days_in_month(year, month):
    if year is True and month is 2:
        return 29
    else:
        return days_month[month - 1]


year = leap_year(int(input("Enter a year: ")))
month = int(input("Enter a month (number): "))


print(days_in_month(year, month))
