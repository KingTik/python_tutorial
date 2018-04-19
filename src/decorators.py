

# New function
def print_number_better(function):
    def inside_function(*number): # pass arguments (the same that are passed while function is called)
        print "The number is: " + str(number[1])
        function(number[0], number[1])
    return inside_function # has to return callable object


#original function + @new function
@print_number_better
def print_number(number, two):
    print number
    

# prints new funcion
print_number(100,11)

# equvalent to 
# print_number = print_number_better(print_number)
