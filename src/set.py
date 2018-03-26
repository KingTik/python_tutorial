'''
set is a collection of unique elements
'''
from sets import Set
#uniqe elements
int_set = Set([1,2,1,3])
print int_set

# in keyword

if 1 in int_set:
    print "Contains! :D"
else:
    print "Doesn't contain :("

#Adding elements
int_set.add(100)
print int_set


#Elements can be different types
int_set.add("hello")
print int_set

#Erase element
int_set.remove("hello")
print int_set



#Set arthmetics
set1 = Set([1,9, 89, 17, 0])
set2 = Set([1,3, 44, 0])

print set1 - set2 
print set1 | set2
print set1 & set2
print set1 ^ set2