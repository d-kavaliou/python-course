# Write a function that accepts two strings as parameters and checks whether these strings are anagrams of each other. 
# An anagram is a text formed by rearranging the letters of another piece of text.

# The strings should not be case-sensitive, meaning that Cats and AcTs are anagrams.

def checkAnagram(str1, str2):
    str1 = list(str1.lower())
    str2 = list(str2.lower())
    for i in str1:
        if i in str2:
            str2.remove(i)
            continue
        else:
            continue
    if str2 == []:
        return 1
    else:
        return -1

    
assert checkAnagram('listen', 'silenT') == 1
assert checkAnagram('Accept', 'except') == -1
assert checkAnagram('triangle', 'integral') == 1
assert checkAnagram('meatS', 'sTeam') == 1
assert checkAnagram('Skin', 'sink') == 1
print ('its ok!')
