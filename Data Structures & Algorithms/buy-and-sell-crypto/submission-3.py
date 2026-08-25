class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        tot=0
        for i in range(len(prices)):
            if mini>prices[i]:
                mini=prices[i]
            else:
                ans=prices[i]-mini
                if tot<ans:
                    tot=ans
        return tot
        