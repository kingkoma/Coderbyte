'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
'''
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_bin = str(bin(num))
        string = ''
        for i in num_bin[2:]:
            
            if i == '0':
                i = '1'
            else:
                i = '0'
            string += i
        return int(string, 2)
        # return int(''.join(str(0) if r == '1' else str(1) for r in bin(num)[2:]), 2)
