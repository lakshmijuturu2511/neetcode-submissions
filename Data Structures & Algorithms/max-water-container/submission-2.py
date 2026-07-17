class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        res=float('-inf')
        while l<r:
            w=r-l
            h=min(height[l],height[r])
            res=max(res,w*h)
            if height[l]<height[r]:
                l+=1
            elif height[l]>=height[r]:
                r-=1
            
        return res
