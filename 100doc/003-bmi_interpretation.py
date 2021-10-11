# body mass index

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    m = "underweight"
elif bmi < 25:
    m = "normal weight"
elif bmi < 30:
    m = "overweight"
elif bmi < 35:
    m = "obese"
else:
    m = "clinically obese"

print(f" Your body mass index is: {bmi}, you are {m}")
