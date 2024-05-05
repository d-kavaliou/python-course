# 125. Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l = []
        for el in s:
            if el.isalpha() or el.isdigit():
                l.append(el)
        new_s = ''.join(l)
        return new_s == new_s[::-1]