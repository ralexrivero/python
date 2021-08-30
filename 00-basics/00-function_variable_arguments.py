#
# function that takes a variable number of arguments
#

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(4, 5, 6, 20, 50, 100))  