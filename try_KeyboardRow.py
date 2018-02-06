'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret_list = []
        a = set('QWERTYUIOP')
        b = set('ASDFGHJKL')
        c = set('ZXCVBNM')
        for word in words:
            w = set(word.upper())
            if (a&w==w) | (b&w==w) | (c&w==w):
                ret_list.append(word)
        return ret_list
