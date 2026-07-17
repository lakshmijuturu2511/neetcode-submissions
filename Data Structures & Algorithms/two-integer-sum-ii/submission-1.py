class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l=0
        r=n-1
        res=[]
        while l!=n-1 and r!=0:
            add=numbers[l]+numbers[r]
            if add > target:
                r=r-1
            elif add<target:
                l=l+1
            elif add==target:
                res.append(l+1)
                res.append(r+1)
                break
        return res