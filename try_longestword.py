"""
Using the Python language, have the function LongestWord(sen) take the sen parameter being passed 
and return the largest word in the string. If there are two or more words that are the same length, 
return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 

"""

def LongestWord(sen): 
    newstr = ''
    for i in sen:
        if i.isalpha() or i.isspace():
            newstr += i
        else:
            del i
    words = newstr.split(' ')
    return max(words, key=len)
    
print(LongestWord(input())) 


