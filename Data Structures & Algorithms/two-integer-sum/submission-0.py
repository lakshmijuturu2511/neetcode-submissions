class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        res=[]
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in d:
                
                res.append(d[diff])
                res.append(i)
                return res
            d[nums[i]]=i
        return -1
