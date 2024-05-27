"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_nums = set(nums)
        if len(nums) == len(set_nums):
            return False
        return True

print(Solution().containsDuplicate([1,2,2,5,6,7,2]))
print(Solution().containsDuplicate([1,2,3,4,5]))