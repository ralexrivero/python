import random
import string

alpha = list(string.ascii_letters)
digits = list(string.digits)
special = list(string.printable[62:94])

print("Welcome to the password generator.")
user_a = int(input("How many letters would you like in your password?\n"))
user_d = int(input("How many numbers would you like?\n"))
user_s = int(input("How many symbols would you like?\n"))
password = []

m = 0
for l in range(0, user_a + user_d + user_s):
    if m <= user_a:
        password.append(alpha[random.randint(0, len(alpha) - 1)])
        m += 1
    elif m <= user_a + user_d:
        password.append(digits[random.randint(0, len(digits) - 1)])
        m += 1
    else:
        password.append(special[random.randint(0, len(special) - 1)])
        m += 1
random.shuffle(password)

for n in password:
    print(n, end='')
print()

password.clear()