'''
Function often seen with lambda functions but not necessarily
map - applys passed function to every element of input
reduce - accumulates result of passed function for every element
filter - returns
'''

def square(x):
    return x*x


input = [1,2,3,4,5]

#pass function
print map(square, input)

#pass lambda
#map example 3rd power of every element
print map(lambda x: x*x*x, input)

#reduce example - sum up elements
print reduce(lambda x,y: x+y, input)


#filter exaple return list of even numbers
print filter(lambda x: x%2==0, input)


