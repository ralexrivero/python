#
# date information
#
from datetime import date
from datetime import time
from datetime import datetime

# datetime objects

def main():
    today = datetime.now()
    print("The current date and time is: ", today)

    t = datetime.time(datetime.now())
    print("The time is: ", t)

if __name__ == "__main__":
    main()