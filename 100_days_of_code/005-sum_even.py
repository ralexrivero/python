user_range = input("Type a range (star and end): ").split()

for u in range(0, len(user_range)):
    user_range[u] = int(user_range[u])

even_sum = 0

for i in range(user_range[0], user_range[1]):
    if i % 2 == 0:
        even_sum += i

print("The total even add is: {:d}".format(even_sum))
