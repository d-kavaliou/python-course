class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        "converting all letters into lowercase letters"
        s1 = list(filter(lambda x: x.isalnum(),s))
        "removing all non-alphanumeric letters"
        s2 = list(reversed(s1))
        "checking the string is polindrom"
        result = lambda s1,s2: True if s1 == s2 else False
        return result(s1,s2)

    
solution = Solution()


print(solution.isPalindrome("A man, a plan, a canal: Panama1"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))