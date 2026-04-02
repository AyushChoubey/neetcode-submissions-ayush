class Solution:
    def recursion(self,amount, coins,i,path):
        if amount < 0:
            return 
        if amount == 0:
            if tuple(path) not in self.dict_: 
                print(path)
                self.dict_[tuple(path)] = 1
                self.result.append(1)
            
            return 

        
        # for  i in coins:

        for idx in range(i, len(coins)):     # 🔥 KEY FIX: range(i, ...) not all coins
            coin = coins[idx]
            path.append(coin)
            self.recursion(amount-coin, coins, idx,path)
            path.pop()

    def recursion2(self,amount,coins,i):

        if i >= len(coins):
            return 0 
        if coins[i]<=amount:
            
            return 1+ self.recursion2(amount - coins[i],coins,i+1)
        else:
            return 0 # self.recursion2(amount,coins,i+1)
        
        

        
        

    # def top_down(self,amount, coins,i,path):
    #       if amount < 0:
    #         return 
    #     if amount == 0:
    #         if tuple(path) not in self.dict_: 
    #             print(path)
    #             self.dict_[tuple(path)] = 1
    #             self.result.append(1)
            
    #         return 

        
    #     # for  i in coins:

    #     for idx in range(i, len(coins)):     # 🔥 KEY FIX: range(i, ...) not all coins
    #         coin = coins[idx]
    #         path.append(coin)
    #         self.recursion(amount-coin, coins, idx,path)
    #         path.pop()
    def bottom_up():
        return 
    def change(self, amount: int, coins: List[int]) -> int:

        self.result = []
        self.dict_ = {}
        # self.T = [[]]
        
        # return self.recursion2(amount,coins,0)
        # print(self.dict_)

        # self.recursion( amount, coins,0,[] )
        # print(self.result)
        # return(len(self.result))

        T = [[0]*(amount+1) for _ in range(len(coins)+1) ]
        for i in range(len(coins)+1):
            T[i][0] = 1

        # print(T)
        coins.sort()
        for i in range(1,len(coins)+1):
            for j in range(amount+1):
                if j>= i:
                    T[i][j]  = T[i][j-coins[i-1]]+ T[i-1][j]

                else: T[i][j] = T[i-1][j]
        print(T)
        return T[-1][-1]
