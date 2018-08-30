

def is_anagram(word1, word2):
    if len(word1) is not len(word2):
        return False

    sortedWord1 = ''.join(sorted(word1))
    sortedWord2 = ''.join(sorted(word2))

    if sortedWord1 == sortedWord2:
        return True
    else:
        return False






print is_anagram("krzysiek", "tomek")
print is_anagram("tomep", "tomek")
print is_anagram("kemot", "tomek")