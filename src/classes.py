
class Custom:
    # class member
    member = 4

    # private class member*
    # this will be name mangled to _Custom__priv so you can still access
    __priv = 1

    # proper method
    def display(self):
        print self.member
        print self.__priv #can access

    # this wont throw error but it will casue errors
    # cant't call this method because python will provide one argument
    # to all methods
    def print_4():
        print 4


#inheritance
class Derived(Custom):
    array = []
    
    # Object constructor
    def __init__(self):
        print 'In constructor'
        self.array = ['a','b','c','d']

    # polimorphism
    def print_4(self):
        print self.array[0] + self.array[1] + self.array[2] + self.array[3]

    def inherited_priv(self):
        print self.member
        print self.__priv #this will throw error - didnt inherit that

    def say_hello(self):
        print "Just want to say hello"

# creating object of a user defined class
obj = Custom()

obj.display()

##
#print obj.__priv this will throw error - no such thing

##
#obj.print_4() this will throw error - no arguments accepted one provided

der_obj = Derived()

der_obj.print_4()

#this class doesnt implement this method so its taken form 
#base class (still can access priv member)
der_obj.display()


# der_obj.inherited_priv()

# use method on class and pass object
Derived.say_hello(der_obj)