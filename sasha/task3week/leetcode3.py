
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #function that make the sum of the squares of its digits
        def kv(n):
            summ = 0
            for i in str(n):
                summ += int(i)*int(i)
            return summ
        #list with squares of number's digits, to stop the cycle
        nums =[]
        while n not in nums:
            nums.append(n)
            n = kv(n)
        #checking a happy number
        if 1 in nums:
            return True
        else:
            return False


solution = Solution()


print(solution.isHappy(19))
print(solution.isHappy(2))
