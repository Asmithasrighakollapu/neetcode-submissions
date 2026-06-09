class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        pow=abs(n)
        ans=1
        for i in range(pow):
            ans=ans*x
        if n<0:
            return 1/ans
        return ans