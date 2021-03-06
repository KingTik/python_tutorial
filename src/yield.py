'''
Generators with yield can provide with set of values
Those values are not stored in memory, they are generated on the fly
When generator is executed it will go to the first occurrence of yield, return value and will pause

'''

## Generator
def fibbon_gen(number):
    first = 1
    second = 1
    next = 0
    for i in range(number):
        next = first + second 
        first = second
        second = next
        yield next # yield next value
        
        
print "Iterate over generator"
for i in fibbon_gen(12):
    print i
    
    
print "Call each value yourself"
zm = fibbon_gen(10)
print next(zm)
print next(zm)
print next(zm)    
