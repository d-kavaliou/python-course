"""Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target."""

def twoSum(nums, target):
    for i in nums:
        for f in reversed(nums):
            if i+f == target and nums.index(i) != nums.index(f):
                a = nums.index(f)   
                b = nums.index(i) 
                return [a,b]
                break
            elif i+f == target and i == f :
                s = nums.index(i)+1
                if nums.index(i) != nums.index(f,s):
                    a = nums.index(f)   
                    b = nums.index(i,a+1)
                    return [a,b]
                    break
                else:
                    return 
                    continue
            else:
                continue


print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
            