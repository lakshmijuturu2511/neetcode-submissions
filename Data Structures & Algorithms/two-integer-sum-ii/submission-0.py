class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        res=[]
        for i,num in enumerate(numbers):
            diff=target-num
            if diff in d:
                res.append(d[diff])
                res.append(i+1)
            d[num]=i+1
        return res