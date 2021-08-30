#
# break and continue statement
#

def main():
    print("break")
    for x in range (5, 10):
        # terminate the loop when reach the value 7
        if (x == 7): break
        print(x)

    print("continue")
    for x in range (5, 10):
        # skips the even values
        if (x % 2 == 0): continue
        print (x)
if __name__ == "__main__":
    main()