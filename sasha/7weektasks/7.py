class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        def product_witho(nums):
            res = 1

            for i in nums:
                if i == 0:
                    continue
                else: 
                    print(nums[1])
                    res = res * i
            return res
        def product_withouto(nums):
            res = 1 
            for i in nums:
                res = res * i
            return res
        output = []
        for i in nums:
            if i == 0:
                output.append(product_witho(nums))
            else:
                output.append(product_withouto(nums)//i)
        return output
       
        


# it doesn work with 0 items lists

s = Solution()

print(s.productExceptSelf([1,3,8,0]))
print(s.productExceptSelf([1,2,3,4,5,9]))

