import random
import pi_module

print(pi_module.pi)

rand_int = random.randint(1, 10)
print(rand_int)

rand_float = random.random()
print(rand_float)

rand_int2 = random.randint(0, 5)
print(rand_int2)

rand_float2 = round(random.random() *5)
print(rand_float2)

lis_len = 0
loto = list()

for i in range(0, 100):
    rep = 0
    num = random.randint(1, 45)
    for j in loto:
        rep =  loto.count(num)
    if rep == 1:
        break
    loto.append(num)
    if len(loto) == 5:
        break

loto.sort()
print(loto)