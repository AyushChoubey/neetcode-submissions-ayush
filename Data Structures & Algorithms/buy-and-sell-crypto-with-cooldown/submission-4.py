# class Solution:
    # def recursion(self,prices,i,j):
    #     if i == len(prices) or j == len(prices):
    #         return 0
    #     print(i,j,'1st')
    #     if i>= j  :
    #         if i-j == 1 and j!=0:
    #             print(i,j,'------')
    #             v1 = self.recursion(prices,i+1,i+1)
    #             # return self.recursion(prices,i+1,i+1)
    #             print(v1, 'cooldown')
    #             return v1
                
    #         else:
    #             return(max(-prices[i]+self.recursion(prices,i,i+1),
            
    #             self.recursion(prices,i+1,i+1)))
    #         # print('BUY')
    #         # v1 = -prices[i]+self.recursion(prices,i,i+1)
    #         # v2 = self.recursion(prices,i+1,i+1)
    #         # print(v1,v2,'B values')
    #         # return max(v1,v2)
    #     else:
    #         return(max(
    #         prices[j]+self.recursion(prices,j+1,j),
    #         self.recursion(prices,j+1,j+1)))
    #         # print('SELL')
    #         # v1 = prices[j]+self.recursion(prices,j+1,j)
    #         # v2 = self.recursion(prices,j+1,j+1)
    #         # print(v1,v2,'s values')
    #         # return max(v1,v2)

#     #  def recursion(self, prices, i, can_buy):
#     #     if i >= len(prices):
#     #         return 0

#     #     if can_buy:
#     #         # Can buy today or skip
#     #         buy = -prices[i] + self.recursion(prices, i + 1, False)
#     #         skip = self.recursion(prices, i + 1, True)
#     #         return max(buy, skip)
#     #     else:
#     #         # Can sell today or skip
#     #         sell = prices[i] + self.recursion(prices, i + 2, True)  # cooldown
#     #         skip = self.recursion(prices, i + 1, False)
#     #         return max(sell, skip)




        
#     def maxProfit(self, prices: List[int]) -> int:
#         self.result = 0
#         self.i = 0
#         self.j = 0
#         return self.recursion(prices,self.i,True)

#         # T = [[0]* len(prices+1) for _ in range(len(prices)+1)]

#         # for i in range(1,len(prices)+1):
#         #     for j in range(1,len(prices)+1):
#         #         T[i].append(max())
        
class Solution:
    def recursion(self,prices,i,j):
        if i == len(prices) or j == len(prices):
            return 0
        if i>= j :

            return(max(-prices[i]+self.recursion(prices,i,i+1),
            
            self.recursion(prices,i+1,i+1)))
        else:
            return(max(
            prices[j]+self.recursion(prices,j+2,j+2),
            self.recursion(prices,j+1,j+1)))

    def recursion(self, prices, i, j):
        if i >= len(prices) or j >= len(prices):  # ✅ fix
            return 0

        if i >= j:
            return max(
                -prices[i] + self.recursion(prices, i, i+1),
                self.recursion(prices, i+1, i+1)
            )
        else:
            return max(
                prices[j] + self.recursion(prices, j+2, j+2),  # ✅ cooldown fix
                self.recursion(prices, i, j+1)
            )
    #bottom-up
    

    #top down

    def td_dp(self,prices,i,j,T):
        if i >= len(prices) or j >= len(prices):  # ✅ fix
            return 0
        if (i,j) in T:
            return T[(i,j)]

        if i >= j:
            T[(i,j)] = max(
                -prices[i] + self.td_dp(prices, i, i+1,T),
                self.td_dp(prices, i+1, i+1,T)
            )
            return(T[(i,j)])
        else:
             T[(i,j)] = max(
                prices[j] + self.td_dp(prices, j+2, j+2,T),  # ✅ cooldown fix
                self.td_dp(prices, i, j+1,T)
            )
             return(T[(i,j)])

    def recursion(self, prices, i, j):
        if i >= len(prices) or j >= len(prices):  # ✅ fix
            return 0

        if i >= j:
            return max(
                -prices[i] + self.recursion(prices, i, i+1),
                self.recursion(prices, i+1, i+1)
            )
        else:
            return max(
                prices[j] + self.recursion(prices, j+2, j+2),  # ✅ cooldown fix
                self.recursion(prices, i, j+1)
            )



        
    def maxProfit(self, prices: List[int]) -> int:
        self.result = 0
        self.i = 0
        self.j = 0
        recur = False
        tddp = False
        budp = True
        self.T = {}

        if recur == True:
            return self.recursion(prices,self.i,self.j)
        if tddp == True:
            self.td_dp(prices,self.i,self.j,self.T)
            print(self.T)
            return self.T[(len(prices)-1,len(prices)-1)]
            # return self.T[(0,0)]
        if budp == True:
        

            # to solve it with DP, we will follow a different approach
            n = len(prices)
            T = [[0] * (n + 2) for _ in range(n + 2)]

            # T = [[0]* len(prices)+2 for _ in range(len(prices)+2)]
            # print(T)

            # return 6
            # subproblem defnition - > MAximum profit you can make starting at day buying selling at day [i][j]
            #here we are starting from last to first n->0, becuase it will be really hard to do it upposite and come of with right
            #subproblem defnition for it.

            for i in reversed(range(len(prices))):
                for j in reversed(range(len(prices))):
                    if i >= j:
                        T[i][j] = max(
                            -prices[i] + T[i][i+1],
                            T[i+1][i+1]
                        )

                    else:
                        T[i][j] = max(
                            prices[j] + T[j+2][j+2],
                            T[i][j+1]
                        )
            print(T)

            return T[0][0]
                   


            