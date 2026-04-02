class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        T= []
        T.append(0)
        T.append(0)
        finish = len(cost)+1

        for i in range(2,finish):
            T.append(min(T[i-1]+cost[i-1],T[i-2]+cost[i-2]))

        return T[finish -1]
        