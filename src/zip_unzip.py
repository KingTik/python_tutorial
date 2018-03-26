'''
Zip will merge two lists into one list of tuples
For example
l1 = [a, b, c]
l2 = [x, y, z]
zip(l1,l2) => [(a,x), (b,y), (c,z)]

'''



City = ['Szczecin', 'Warszawa', 'Berlin', 'New York']
Population = [0.4, 1.7,  3.4, 8.5]
print "\nZIPING"
zipped = zip(City, Population)
print "Zipped: "
print zipped

print "\nITERATING"
#easy for iterating
for city, pop in zipped:
    print city + " has " + str(pop) + " mln citizens"


#Unzipping
print "\nUNZIPING"
C, P = zip(*zipped)
print "Unziped City:"
print C
print "Unziped Population: "
print P

