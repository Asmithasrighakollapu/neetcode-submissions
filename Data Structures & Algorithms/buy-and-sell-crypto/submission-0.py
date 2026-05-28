class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if mini>prices[i]:
                mini=prices[i]
            else:
                new_pro=prices[i]-mini
                if profit<new_pro:
                    profit=new_pro
        return profit




        