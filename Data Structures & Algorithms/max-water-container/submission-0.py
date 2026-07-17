class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        res=float('-inf')
        for i in range(n):
            for j in range(i,n):
                w=j-i
                h=min(heights[i],heights[j])
                res=max(res,w*h)
        return res