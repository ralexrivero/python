# and, or , not

# and: both condition must be true

a = 12
print("-" * 40)
print("and")
print("-" * 40)
operator = a > 15 and a > 10
print(operator)

operator = a > 10 and a < 15
print(operator)

operator = a > 15 and a < 20
print(operator)

# or: true ir one or two conditions are true
print("-" * 40)
print("or")
print("-" * 40)

operator = (a == 12 or a > 20)
print(operator)

operator = a == 13 or a < 1
print(operator)

#not reverses the condition: false come true and true come false
print("-" * 40)
print("not")
print("-" * 40)
operator = not a
print(operator)

operator = not a < 1
print(operator)
