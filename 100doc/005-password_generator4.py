import random
import string

alpha = list(string.ascii_letters)
digits = list(string.digits)
special = list(string.printable[62:94])
print(special)
print("Welcome to the password generator.")
user_a = int(input("How many letters would you like in your password?\n"))
user_d = int(input("How many numbers would you like?\n"))
user_s = int(input("How many symbols would you like?\n"))
password = []

for c in range(user_a + user_d + user_s):
    if c < user_a:
        password.append(random.choice(alpha))
    elif c < user_a + user_d:
        password.append(random.choice(digits))
    else:
        password.append(random.choice(special))

random.shuffle(password)

for c in password:
    print(c, end='')
print()