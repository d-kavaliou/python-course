# 191. Number of 1 Bits

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_n = bin(n)
        result = 0
        for el in bin_n[2:]:
            if el == '1':
                result += 1
        return result
    
        # bin_n = []
        # while n > 0:
        #     remainder = n % 2
        #     bin_n.append(remainder)
        #     n //= 2
        # return sum(bin_n)


print(Solution().hammingWeight(2147483645))
print(Solution().hammingWeight(11))        