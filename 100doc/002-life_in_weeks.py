# your life in weeks

age = input("What is your current age?")
age_i = int(age)
days = (98 - age_i) * 365
weeks = (98 - age_i) * 52
months = (98 - age_i) * 12
message = f"You have {days} days, {weeks} weeks and {months} months left"

print(message)