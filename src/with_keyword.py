'''
With keyword guarantees safe execution of code.
If you have some resources that need to be controlled (like files)
consider using this technique

'With' will call __exit__ method even if exception was thrown somewhere
in the code
'''


class ControlledObj:
    
    #Method called at the beginning of with statement
    def __enter__(self):
        print "Object was created and resources allocated"
        
    #method called at the end of with statement or when exception is thrown
    #type, value and traceback arguments are informations about exception if it occurred (else they are none)
    def __exit__(self, type, value, traceback):
        print "Object was destroyed and resources released"


print "Before with"
with ControlledObj() as instance:
    print "Inside with statement"
    # print 1/0 #this throws exception
    
print "After with"