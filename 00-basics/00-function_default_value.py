#
# function with default value
#

def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# if dont pass x, the default will be 1
print(power(2))
print(power(2,3))
print(power(3,4))
# supply the name of the values. Dont need to pass in a particular order if use names 
print(power(x = 4, num = 3))