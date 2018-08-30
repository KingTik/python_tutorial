class stack:

    def __init__(self): #initialize variables
        self.__data = []
        self.__size = 0
        self.__empty = True

    def push(self, value):  
        self.__data.append(value)
        self.__size = self.__size+1
        
        if True == self.__empty: # flip flag if necessery 
            self.__empty = False

        return True # everything went fine


    def pop(self):
        if False == self.__empty: #if its not empty
            retVal = self.__data.pop()

            self.__size = self.__size - 1 #bookkeeping 
            if self.__size == 0:
                self.__empty = True
        else:
            return None

        return retVal

    def size(self):
        return self.__size

    def empty(self):
        return self.__empty



newStack = stack()

newStack.push(5)
newStack.push(6)
newStack.push(7)
newStack.push(8)
newStack.push(9)
newStack.push(10)
newStack.push(11)

while True:
    var = newStack.pop()
    if var is None:
        break
    else:
        print var