
# function definition
def foo(arg1, arg2):
    print arg1
    print arg2
    return arg1+arg2, arg2+arg1 #multiple return variables

print foo("ala", " ma kota ")


#passing undefined amount of arguments
def bar(*args):
    print "number of arguments: " + str(len(args))
    for argument in args:
        print argument
bar(1,2,3,4,5)
bar("pepe", "the", "frog")


#default arguments
#non default arguments cant be before default arguments
#def foobar(arg1 = 1, arg2):  <- this will fail
def foobar(arg1, arg2=1):
    print arg1
    print arg2

foobar(-9)
foobar(100,99)

# immutable vs mutable 

def iFunc(integer):
    integer += 1

def sFunc(string):
    string+="!"

def aFunc(in_array):
    in_array[0] += "!"
    in_array.append("next")

var = 1
svar = "ala"
a = ["element", "element2"]

iFunc(var) #immutable
print var

sFunc(svar) #immutable
print svar

aFunc(a) #mutable
print a

def listFunc(l = []): # careful with immutable as default arg
    print l
    l.append(1)

listFunc()
listFunc()
listFunc()

'''
immutable types:
    int
    float
    decimal
    complex
    bool
    string
    tuple
    range
    frozenset
    bytes

mutable types:
    list
    dict
    set
    bytearray
    user-defined classes (unless specifically made immutable)

source: https://codehabitude.com/2013/12/24/python-objects-mutable-vs-immutable/
'''
