class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        tot=0
        for i in range(1,len(prices)):
            if mini>prices[i]:
                mini=prices[i]
            else:
                c=prices[i]-mini
                if tot<c:
                    tot=c
        return tot
        