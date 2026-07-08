
class Solution:
    def sumofsquares(self,num):
        y=0
        while num>0:
            x=num%10
            y=y+(x*x)
            num=num//10
        return y
    def isHappy(self, n: int) -> bool:
        res=self.sumofsquares(n)
        seen=set()
        seen.add(n)
        seen.add(res)
        while res!=1:
            res=self.sumofsquares(res)
            if res in seen:
                return False
            seen.add(res)
        return True