#
# working with date information
#
# from the datatime standard module, with comes from the standrd library import classes 
from datetime import date
from datetime import time
from datetime import datetime

#DATE OBJECTS
def main():
    # today() method
    today = date.today()
    print("Today's date is:", today)

    # date individual components
    print("Date components:", today.day, today.month, today.year)

    # retrieve today's week (0 = Monday, 6 = Sunday)
    print("Today's weekday # is:", today.weekday())
    days = ["mon", "tue", "wed", "thu", "fri", "sat"]
    print("Which is a:", days[today.weekday()])

if __name__ == "__main__":
    main()