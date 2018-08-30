
#returns True/False
def pesel_is_valid(pesel):
    t = [int(x) for x in pesel]
    sum = t[0]*1 + t[1]*3 + t[2]*7 + t[3]*9 + t[4]*1 + t[5]*3 + t[6]*7 + t[7]*9 + t[8]*1 + t[9]*3
    mod =  sum % 10
    if 10-mod == t[10]:
        return True
    else:
        return False
    
#         [valid, gender, day, month, year]
# returns [False, None, None, None, None] i pesel i incorrect
# returns [True, "F/M", Day, Month, Year]

def pesel_check(pesel):
    mapping = {0: 1900, 1: 1900, 2: 2000, 3: 2000, 4:2100, 5: 2100, 6:2200, 7:2200, 8: 1800, 9: 1800} # maps month modulo to year
    
    if (len(pesel) != 11):
        return [False, None, None, None, None]

    if pesel_is_valid(pesel) == False: # passing pesel with correct length
        return [False, None, None, None, None]

    year = int(pesel[0:2]) 
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    
    try:
        year = year + mapping[month//10]
    except KeyError:
        print month//10
        return [False, None, None, None, None] 

    if int(pesel[9]) % 2 == 0:
        gender = "F"
    else:
        gender = "M"

    return [True, gender, day, month, year]
    



retVal = pesel_check("25923072101") # correct
print retVal
retVal = pesel_check("11210524411") # correct
print retVal
retVal = pesel_check("11461963809") # correct
print retVal
retVal = pesel_check("44051401358") # not correct
print retVal
retVal = pesel_check("91123011417") # correct
print retVal
