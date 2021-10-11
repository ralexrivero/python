print("Welcome to the leap year evaluator!")
year = int(input("Which year do you want to check?: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            m = "leap"
        else:
            m = "not leap"
    else:
        m = "leap"
else:
    m = "not leap"

print(f"The year {year} is {m}")