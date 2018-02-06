'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s_list = s.split()
        # new_list = []
        # for word in s_list:
            # word = word[::-1]
            # new_list.append(word)
        # return ' '.join(new_list)
    
        return ' '.join(word[::-1] for word in s.split())
