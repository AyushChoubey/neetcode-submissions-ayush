class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        T = [[0]*(n+1) for _ in range (m+1)]
        

        for i in range(1,m+1):
            for j in range(1,n+1):
                if i ==1 and j == 1:
                    T[i][j] = 1
                else:
                    # print('bitch',T[i][j], T[i-1][j],T[i][j-1] ,i,j)
                    T[i][j] = T[i-1][j]+T[i][j-1] 


        # print(T)
        return T[-1][-1]

        