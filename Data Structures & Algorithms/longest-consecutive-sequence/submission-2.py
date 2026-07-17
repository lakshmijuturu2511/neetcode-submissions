class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        maxCount=0
        for num in numSet:
            if num-1 not in numSet:
                count=1
                while num+1 in numSet:
                    num=num+1
                    count+=1
                maxCount=max(maxCount,count)
        return maxCount