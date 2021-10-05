# tip calculator

print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
percent = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

bill_f = float(bill)
percent_f = float(percent)
people_i = int(people)
pay = round(bill_f * (1 + percent_f / 100) / people_i, 2)
message = f"Each person should pay: $ {pay}"
print(message)