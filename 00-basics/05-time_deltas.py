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

#printf more arguments
print("In 5 days and 2 weeks, it will be:" + str(now + timedelta(days = 5, weeks = 2)))

#calculate 2 weeks ago
t = datetime.now() - timedelta(weeks = 1)
