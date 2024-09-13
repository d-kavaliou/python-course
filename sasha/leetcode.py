"""Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
def twoSum(nums, target):
        result = {} 
        for i, num2 in nums: 
            num1 = target - num2 
            if num1 in result: 
                return [result[num1], i]
            result[num1] = i 
        return None 


print(twoSum([2,7,11,15],9))"""
#print(twoSum([3,2,4],6))
#print(twoSum([3,3],6))
a = "3.65  3.91  1.71  2.31  3.60  6.38  2.95  3.31  8.53  0.81  4.28  7.91  2.43  6.21  2.30 -0.98  0.65  1.94  5.19  4.44  3.01  6.04  2.47  0.39  4.54 7.55  2.56  4.60  4.17  6.36  2.47  2.99  5.25  1.98  5.55  5.87  2.42  3.79  4.68  2.91  4.36  2.57  1.89  5.83  6.38  7.55  2.42  2.74  4.97  3.45 1.56  3.51  1.74  4.91  7.67  2.11  4.71  1.86  7.26  4.89  5.59  6.19  0.41  6.61  6.88  3.92  3.03  4.54  8.83  6.32  3.65  3.86  5.55  5.25  2.93 5.67  5.86  5.02  2.23  5.00  4.74  7.57  5.09  4.09  9.26  5.25  4.43  2.77  4.16  0.64  3.58  3.66  4.70  5.58  3.55  1.70  3.13  7.72  4.99  4.60"
b = a.split(' ')
c = []
for i in b:
    if i != "":
            c.append(float(i))
    else:
        continue
cb = set(c)
b = list(cb)
b.sort()
r = list(range(1,90))
r.reverse()
for i in r :
    print (1/i)


