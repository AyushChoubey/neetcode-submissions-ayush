class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1d solution 

        T = [amount+1] *(amount+1)
        T[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if c<=i:
                    T[i] = min(T[i],1+T[i-c])

        print(T)
        
        return T[-1] if T[-1]!= amount+1 else -1