# converts the num to hours:minutes


# mine python3
def TimeConvert(num):

    hours = int(num)//60
    minutes = (int(num)-hours*60)
    return '{}:{}'.format(hours, minutes)

    # others python2
    # return str(num / 60) + ':' + str(num % 60)
    # return ':'.join([str(num/60), str(num%60)])


print(TimeConvert(input()))
