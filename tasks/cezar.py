

# can use ord() function
def cezar(text):
    alphabet = ["a", "b", "c", "d" ,"e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "v", "x", "y", "z"]
    newText = ""
    for letter in text:
        
        if str(letter) in alphabet:
            index = alphabet.index(letter)
            newLetter = alphabet[ (index + 3)% len(alphabet) ]            
        else:
            newLetter = letter

        newText = newText + newLetter

    return newText



# jakie sa minusy tego rozwiazania?
# jakie sa plusy tego rozwiazania?

print cezar("tomasz")
print cezar("ala ma kota")