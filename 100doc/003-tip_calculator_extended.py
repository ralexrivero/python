print("Welcome to the tip calculator")

height = int(input("What is your height? (in cmts) "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult ticket are $12")
    
    photo = input("Do you want a photo? Y or N ")
    if photo == 'Y':
        bill += 3

    print(f"Your total bill is: ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride")

