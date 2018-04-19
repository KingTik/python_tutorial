
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



'''
Overloading:

__add__(self, other)                                a1 + a2
__sub__(self, other)                                a1 - a2
__mul__(self, other)                                a1 * a2
__matmul__(self, other)                             a1 @ a2 (Python 3.5)
__div__(self, other)                                a1 / a2 (Python 2 only)
__truediv__(self, other)                            a1 / a2 (Python 3)
__floordiv__(self, other)                           a1 // a2
__mod__(self, other)                                a1 % a2
__pow__(self, other[, modulo])                      a1 ** a2
__lshift__(self, other)                             a1 << a2
__rshift__(self, other)                             a1 >> a2
__and__(self, other)                                a1 & a2
__xor__(self, other)                                a1 ^ a2
__or__(self, other)                                 a1 | a2
__neg__(self)                                       -a1
__pos__(self)                                       +a1
__invert__(self)                                    ~a1
__lt__(self, other)                                 a1 < a2
__le__(self, other)                                 a1 <= a2
__eq__(self, other)                                 a1 == a2
__ne__(self, other)                                 a1 != a2
__gt__(self, other)                                 a1 > a2
__ge__(self, other)                                 a1 >= a2
__getitem__(self, index)                            a1[index]
__contains__(self, other)                           a2 in a1
__call__(self, *args, **kwargs)                     a1(*args, **kwargs)

source: http://goalkicker.com/PythonBook/
'''


## Initializing outside __init__
class whereToInitialize:
    value = {}

whereIndeed1 = whereToInitialize()
whereIndeed1.value['hello'] = "world" # put in on one instance
whereIndeed2 = whereToInitialize()
print whereIndeed2.value['hello'] # another instance still has access (static)
#--
class whereToInitializeInit:
    def __init__(self):
        self.value = {}


whereIndeed1 = whereToInitializeInit()
whereIndeed1.value['hello'] = "world"
whereIndeed2 = whereToInitializeInit()
# print whereIndeed2.value['hello']  # keyerror!

