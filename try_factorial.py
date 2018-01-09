def FirstFactorial(num):
    try:
        num = int(num)
    except ValueError as e:
        print('number only')
    else:
        if num < 1 or num > 18:
            print('The num should between 1 and 18')
        else:
            refer = 1
            for i in range(1, num+1):
                refer *= i
            # code goes here
            return refer

if __name__ == '__main__':
    # keep this function call here
    print(FirstFactorial(input('please input number:')))

