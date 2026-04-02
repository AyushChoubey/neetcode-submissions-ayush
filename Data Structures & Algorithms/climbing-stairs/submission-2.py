class Solution:
    def climbStairs(self, n: int) -> int:

        T = []
        
        T.append(1)
        T.append(1)

        for i in range(2,n+1):
            T.append(T[i-1]+T[i-2])

        return(T[n])            
    




        