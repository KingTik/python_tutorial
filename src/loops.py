

### for loop
# with range() function
stri = ""
for i in range(5):
    stri += str(i) + " "
print stri

stri = ""
for i in range(5,10):
    stri += str(i) + " "
print stri

# iterating over list, dictionary, map etc 
stri = ""
custom_list = ['a', 'b', 'c', 'd']
for i in custom_list:
    stri += i + " "
print stri

# with enumerate
for number, element in enumerate(custom_list):
    print str(number) + " - " + str(element) 



### while loop
i = 0
stri = ""
while i<5:
     stri+=str(i)
     i+=1
print stri

### loops can have else statement
i = 5
stri = ""
while i<5:
     stri+=str(i)
     i+=1
else:
    print "Didnt went into loop"
print "stri: " + stri
