class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <2 :return 0
        max_profit = 0
        i = 0
        for j in range(1,len(prices)):
            profit = prices[j] - prices[i]
            if profit <0:
                i=j
            
            else:
                if  profit > max_profit:
                     max_profit = profit

        
        return max_profit

            