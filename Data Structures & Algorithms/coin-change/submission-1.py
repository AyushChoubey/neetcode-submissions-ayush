class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        T = [[float("inf")]*(amount+1) for _ in range(len(coins)+1)]

        for i in range(len(coins)+1):
            T[i][0] = 0

        # print(T)
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                # print(i,j,coins[i-1],T[i][j],T[i][j-coins[i-1]])
                if j>=coins[i-1]:
                    T[i][j] = min(1+T[i][j-coins[i-1]], T[i-1][j])
                else:
                    T[i][j] = T[i-1][j]
                    # print(T[i][j],T[i-1][j],i,j,coins[i-1],coins)

        
        # print(T)
        if T[-1][-1] != float("inf"):
            return T[-1][-1]
        else: 
            return -1
        