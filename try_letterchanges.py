
# ie. c -> d, z -> a, capitalize every vowel(aieuo) in new string

def LetterChanges(str):
    new_str = ''
    for i in str:
        if i.isalpha():
            if i == 'z':
                i = 'a'
            elif i == 'Z':
                i = 'A'
            else:
                i = chr(ord(i) + 1)
                if i in 'aeiou':
                    i = i.upper()
        else:
            i = i
        new_str += i
    # code goes here
    return new_str


# keep this function call here
print(LetterChanges(input()))

