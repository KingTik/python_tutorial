'''
Dictionaries in python
'''
#initialization
my_dict = {'meme': 'pepe', 'key': 'value'}
my_dict = {} 
#insert item
my_dict["key"] = 5
my_dict["key2"] = 4


##loop over
#just keys
for key in my_dict:
    print "key: " + str(key)

for value in my_dict.values():
    print "value: " + str(value)

for key, value in my_dict.items():
    print "key: " +str(key) + " value: " + str(value)



## defaultdict
# if "this" not in my_dict:
#     my_dict["this"] = 1
# else:
#     my_dict[this] +=1
from collections import defaultdict
my_dict = defaultdict(lambda: 0)
print my_dict["hello"]

## try - except
my_dict = {}
try:
    print my_dict['key']
except KeyError:
    print 'No such key!'

# instead of:
# if 'key' in my_dict:
#   print my_dict['key']
# else:
#   print 'no such key!'