class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        i = 0
        j= 1

        while j != len(prices):
            if prices[j]>prices[i]:
            
                profit = max(profit,prices[j]-prices[i])
            else:
                i= j
            j+=1
        
        return profit
            