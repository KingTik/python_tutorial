'''
Del keyword removes vairable from local and global namespace

'''



foo = 4
del foo
# print foo  #error: foo is not defined

#be careful with loops
tab = [1,2,3,4,5,6,7]
for i, elem in enumerate(tab):
    #del elem # error!
    print elem

#del slice of table
#erases tab<start, stop)
del tab[2:4]
print tab