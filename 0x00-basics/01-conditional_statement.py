#
# conditional statement in one line
#

def main():
    x, y = 1000, 100
    # a if C else b
    st = "x is less than y" if (x < y) else "x is greater than y"
    print(st)

if __name__ == "__main__":
    main()