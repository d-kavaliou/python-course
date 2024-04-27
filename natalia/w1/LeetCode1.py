class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                result = nums[i] + nums[j]
                if result == target:
                    return [i,j]
                j += 1
            i += 1

#examples
print(Solution().twoSum([2,7,11,15],9))
print(Solution().twoSum([3,2,4],6))
print(Solution().twoSum([3,3],6))