class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        l=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]+prices[j]<=money:
                    ans=prices[i]+prices[j]
                    l.append(money-ans)
        if len(l)==0:
            res=money
        else:
            res=max(l)

        return res
        

        