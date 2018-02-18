"""
Given number n. Print number from 1 to n. But:
when number is divided by 3, print "fizz".
when number is divided by 5, print "buzz".
when number is divided by both 3 and 5, print "fizz buzz".
"""

class Solution:
    """
    @param: n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        li = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 != 0:
                li.append('fizz')
            elif i%5 == 0 and i%3 != 0:
                li.append('buzz')
            elif i%3 == 0 and i%5 == 0:
                li.append('fizz buzz')
            else:
                li.append(str(i))
        return li
    
    
# method 2
        return ['Fizz' * (not i%3) + 'Buzz' * (not i%5) or str(i) for i in range(1, n+1)]
                        
                        
if __name__ == '__main__':
    s = Solution()
    s.fizzBuzz(15)
    
