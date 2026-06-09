class Solution:
    def isHappy(self, n: int) -> bool:
        l=set()
        sum=0
        while n!=1:
            if n in l:
                return False
            l.add(n)
            sum=0
            while n>0:
                rem=n%10
                sum+=rem**2
                n=n//10
            n=sum
        return True
            


        