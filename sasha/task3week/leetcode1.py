"""Given an integer array nums, return true if
any value appears at least twice in the array,
and return false if every element is distinct."""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """for num in nums:
            if nums.count(num)>1:
                result = True
                break
            else:
                result = False
                continue
        return result"""
        #Another way
        #create a set with unique numbers
        if len(set(nums)) == len(nums):
            return True
        else:
            return False
        
        

#1)time complexity O(n^2)/15ms
#2)O?/16ms????


solution = Solution()


print(solution.containsDuplicate([1,2,3,1]))
print(solution.containsDuplicate([1,5,-2,-4,0]))
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
        