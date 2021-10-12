print("Welcome to the Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
extra = input("Do you want extra cheese? Y or N ")

bill = 0

if (size == 'S'):
    bill += 15
    if (pepperoni == 'Y'):
        bill += 2
elif (size == 'M'):
    bill += 20
    if (pepperoni == 'Y'):
        bill += 3
elif (size == 'L'):
    bill += 25
    if (pepperoni == 'Y'):
        bill += 3
if (extra == 'Y'):
    bill += 1

print(f"Your final bill is: ${bill}")
