"""
202. Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

class Solution(object):
    def isHappy(self, n, set_for_check=None):
        """
        :type n: int
        :rtype: bool
        """
        if set_for_check is None:
            set_for_check = set()
        if n == 1:
            return True
        if n in set_for_check:
            return False
        set_for_check.add(n)
        list_of_sq = [int(el) ** 2 for el in str(n)]
        result = sum(list_of_sq)
        return self.isHappy(result, set_for_check)

        
print(Solution().isHappy(9))
print(Solution().isHappy(7))
print(Solution().isHappy(19))