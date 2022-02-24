#
# timedelta objects
#
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days = 365, hours = 5, minutes = 1))

# print today's date

now = datetime.now()
print("Today is: " + str(now))

# print today's day date one year from now
print("One year from now it will be: " + str(now + timedelta(days = 365)))

# printf more arguments
print("In 5 days and 2 weeks, it will be:" + str(now + timedelta(days = 5, weeks = 2)))

# calculate 69 weeks ago formatted as string
t = datetime.now() - timedelta(weeks = 69)
s = t.strftime("%A %B %d, %Y")
print("69 weeks ago was: " + s)

# how many days until my birthday
# today
today = date.today()
# my birthday
brt = date(today.year, 9, 24)

# compare to see if the target day is gone for this year
# if it has, use the replace() function to get the date for next year
if brt < today:
        print("My birthday already went by %d days ago" % ((today - brt).days))
        brt = brt.replace(year = today.year + 1)

# calculate the amount of time until birthday
time_to_brt = brt - today
print("It's just: ", time_to_brt.days, "days until my birthday")