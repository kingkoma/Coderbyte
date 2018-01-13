"""
Take any four digit number (whose digits are not all identical), and do the following:
Rearrange the string of digits to form the largest and smallest 4-digit numbers possible.
Take these two numbers and subtract the smaller number from the larger.
Use the number you obtain and repeat the above process.
"""

def KaprekarsConstant(num):
    counts = 0
    num = int(num)
    while num != 6174:
        new_num = '%04d' % num
        num = int(''.join(sorted(new_num, reverse=True))) - int(''.join(sorted(new_num)))
        counts += 1
    return counts

print(KaprekarsConstant(input()))
