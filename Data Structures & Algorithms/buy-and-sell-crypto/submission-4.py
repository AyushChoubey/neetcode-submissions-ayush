class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # T = [[0]*len(prices)]*2
        # T[1][0] = 101

        T = [0]*(len(prices)+1)
        T[0] = 101

        profit = 0
        # print(T)

        #T[0][i] = max sell price till ith position
        #T[1][i] = min buy price till ith position

        for i in range(1, len(prices)+1):
            # T[0][i] = max(T[0][i-1],prices[i-1])
            T[i] = min(T[i-1],prices[i-1])
            profit = max(profit, prices[i-1]-T[i])
            print(profit)
        
        return profit