"""The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum
of the two preceding ones, starting from 0 and 1. That is,"""
class Solution(object):
    def fib(self,n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

solution = Solution()

print(solution.fib(2))
print(solution.fib(3))
print(solution.fib(4))