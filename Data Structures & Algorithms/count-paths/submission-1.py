class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # sub problem defnition 
        # all possible unique paths to reach [i][j] from [0][0] = T[i][j]
        #Initialization 
        T = [[] for i in range(m)]
        for i in range(1,m):
            T[i].append(1)
        T[0].append(1)# erliar I thought it should be 0 but it should be one
        #to be honest it doen't matter but we assume if there i just 1,1 grid it takes 1 
        for i in range(n):

             T[0].append(1)

        for i in range(1,m):
            for j in range(1,n):
                # print(T[i-1][j],T[i][j-1])
                T[i].append(T[i-1][j]+T[i][j-1])

        return T[m-1][n-1]
        
