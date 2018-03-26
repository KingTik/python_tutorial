'''
Basic mathematic operations in python
'''


n1, n2 = 7.0, 2.0
print "Adding"
print str(n1) + " + " + str(n2)+ " = " + str(n1+n2) + '\n'
print "Subtracting"
print str(n1) + " - " + str(n2)+ " = " + str(n1-n2)+ '\n'
print "Multiplying"
print str(n1) + " * " + str(n2)+ " = " + str(n1*n2)+ '\n'
print "Dividing"
print str(n1) + " / " + str(n2)+ " = " + str(n1/n2)+ '\n'
print "Dividing and rounding down"
print str(n1) + " // " + str(n2)+ " = " + str(n1//n2)+ '\n'
print "Power" # Also can use pow() function
print str(n1) + " ** " + str(n2)+ " = " + str(n1**n2)+ '\n'
print "Modulo" 
print str(n1) + " % " + str(n2)+ " = " + str(n1%n2)+ '\n'


number = 1234567
print "\ndivmod example: every digit of " + str(number)
#print every digit of a number


while(number):
    number, mod = divmod(number, 10) # divmod returns (number//10, number%10)
    print mod
