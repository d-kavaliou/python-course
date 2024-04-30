"""Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target."""
def twoSum(nums, target):
        result = {} 
        for i, num2 in nums: 
            num1 = target - num2 
            if num1 in result: 
                return [result[num1], i]
            result[num1] = i 
        return None 


print(twoSum([2,7,11,15],9))
#print(twoSum([3,2,4],6))
#print(twoSum([3,3],6))
            