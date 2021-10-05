# measure of body composition

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = float(weight) / float(height) ** 2
bmi_i = int(bmi)
print("your BMI is: " + str(bmi_i))