#
# Declaring variables
#

# Declare and initilize a variable

f = 0
print(f)

# Redeclaring variable it will override the previous value

f = "abc"
print(f)

#ERROR: can't combine diferent types

# print("this string can not be combined with numbers" + 123)

# Convert a string to a number and combine works propperly

print(f + str(123))

# Global variables vs local variables

# print "def"
def exampleFunction():
        global f
        f = "def"
        print(f)

# printf "abc", but if f is global will print "def"
exampleFunction()
print(f)

# delete a variable

del f
# cause an error because f is not defined
print(f)