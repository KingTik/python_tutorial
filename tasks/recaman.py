
# https://oeis.org/search?q=recaman&sort=&language=english&go=Search


howManyElements = 15
sequence = []
sequence.append(0) 


for i in range(1,howManyElements):
    
    if sequence[i-1] - i not in sequence and (sequence[i-1] - i) > 0:        
        sequence.append( sequence[i-1] - i )
    else:
        sequence.append( sequence[i-1] + i )


print sequence