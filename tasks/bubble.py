


def bubble(data):
    newData = data
    length = len(data)
    
    if length < 2:
        return data

    for i in range(length):
        for j in range(i+1, length):
            if newData[i] > newData[j]:

                tmp = newData[i]
                newData[i] = newData[j]
                newData[j] = tmp

    return newData



print bubble([5,1,4,15,12,0, 3])
