'''
Lambda functions:
- can't be multilined
- can be assigned to variable
- can be called like normal function
- can return more that 1 value
- can be passed to finction 
'''

def pass_lambda_here(your_lambda):
    return your_lambda(5)

#syntax
l1 = lambda x: x *2
print l1(5)

#return list
l2 = lambda x: [x/10, x%10]
print l2(11)

#return tuple
l2 = lambda x: (x/10, x%10)
print l2(11)

print pass_lambda_here(lambda x: "hello "*3 )