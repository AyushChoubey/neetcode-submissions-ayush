class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # recursion:

        T = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]

        for i in range(len(word2)+1):
            T[0][i] = i
        for i in range(len(word1)+1):
            T[i][0] = i
            


        for i in range (1,len(word1)+1):
            for j in range(1,len(word2)+1):

                if word1[i-1] == word2[j-1]:


                    T[i][j] = min(1+T[i-1][j],1+T[i][j-1],T[i-1][j-1])
                else:
                    T[i][j] = min(1+T[i-1][j],1+T[i][j-1],1+T[i-1][j-1])


        return T[-1][-1]

                
        