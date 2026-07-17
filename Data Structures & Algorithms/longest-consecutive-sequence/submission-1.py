class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        maxcount=float('-inf')
        for num in nums:
            count=1
            while num+1 in nums:
                count+=1
                num=num+1
            maxcount=max(count,maxcount)
        return maxcount

            

