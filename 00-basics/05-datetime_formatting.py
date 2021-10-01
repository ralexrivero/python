#
# formatting time and date output
#

from datetime import datetime

def main():

### DATE FORMATTING ###
    now = datetime.now()
# %y/%Y = year, %a/%A - weekday, %b/%B - month, %d = day of month
    # use a place holder to format datetime
    print(now.strftime("The current year is: %Y"))
    # use several codes
    print(now.strftime("%a, %d %B, %y "))

# %c - locale's date and time, %x - locale's date, %X - locale's time
# use local setting on this computer, for that may vary in other settings areas
# uses of local may be: 2021-08-30 or maybe 30-08-2-21 or 08-30-2021
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))

### TIME FORMATTING ###
# %I/%H - 12/24 hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S - %p"))
    print(now.strftime("24-hour time: %H:%M"))
if __name__ == "__main__":
    main()