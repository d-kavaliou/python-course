# 509. Fibonacci Number

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

print(Solution().fib(1))
print(Solution().fib(2))        
print(Solution().fib(6))
print(Solution().fib(8))