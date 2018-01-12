"""
Using the Python language, have the function AlphabetSoup(str) take the str string parameter 
being passed and return the string with the letters in alphabetical order (ie. hello becomes ehllo). 
Assume numbers and punctuation symbols will not be included in the string. 
"""


def AlphabetSoup(str):
    # method1 sort()
    lstr = list(str)
    lstr.sort()
    return ''.join(lstr)
    
    # method2 sorted()
    # return ''.join(sorted(str))


print(AlphabetSoup(input()))
