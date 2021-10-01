#
# super class
#
class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)

# anotherClass is inherit from myClass
# is based on other class (heredada)
class anotherClass(myClass):
    def method1(self):
        # call the inherit method on the super class
        myClass.method1(self)
        print("anotherClass method1")
    
    def method2(self, someString):
        print("anotherClass method2 ")

def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    # the argument passed is not been used
    # because is not calling the inherited method
    c2.method2("this is other string")

if __name__ == "__main__":
    main()