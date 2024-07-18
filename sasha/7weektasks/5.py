class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic ={}
        res=[]
        res2 = []
       
        for i in range(len(nums)):
            dic[nums[i]]=nums.count(nums[i])
        
        for value in dic.values():
            res.append(value)
        res = list(reversed(sorted(res)))
        while len(res)!=k:
            res.pop()
        
        for key, value in dic.items():
                if value in res:
                     res2.append(key)
        return res2
        
      

s = Solution()

print(s.topKFrequent([1,3,3,3,3,2,2,],2))
s.topKFrequent([1,2],2)

