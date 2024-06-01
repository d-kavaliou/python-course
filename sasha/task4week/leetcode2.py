class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = str(bin(n))
        return result.count('1')
        

solution = Solution()


print(solution.hammingWeight(11))
print(solution.hammingWeight(128))
print(solution.hammingWeight(2147483645))

