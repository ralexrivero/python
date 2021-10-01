#
# define basic function
#

# : indicates the start of the functino scope
def func1():
    # indent by 4 spaces indicate the scope started by : (colon)
    print("I am a function")

# call func1
func1()
# func1 dont return a value, because of that, print "None"
print(func1())
# printf the value of the function definition itself
# this demostrate that functions are objects
print(func1)