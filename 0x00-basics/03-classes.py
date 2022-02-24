#
# using classes
#

# define a simple base class
class myClass():
    # inside the class define functions
    # in object oriented terminology they are called method as part of the class
    # the first argument of a method of a class is "self"
    # refer to the object itself
    def method1(self):
        print("myClass method")

    def method2(self, somestring):
        print("myClass method2 " + somestring)

def main():
    # instanciate the class with "c."
    c = myClass()
    # call methods in the class
    c.method1()
    # when call class method don't have to supply the self keyword
    # it will be supply by the python run time
    c.method2("This is a string")

if __name__ == "__main__":
    main()
