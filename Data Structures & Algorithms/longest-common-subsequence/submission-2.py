class Solution:
    def recursion(self,text1,text2,i,j):
        if i  == len(text1)  or  j == len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1+ max(self.recursion(text1,text2,i+1,j),
        self.recursion(text1,text2,i,j+1),
        self.recursion(text1,text2,i+1,j+1))
        else:
           return 0 + max(self.recursion(text1,text2,i+1,j),
            self.recursion(text1,text2,i,j+1),
            self.recursion(text1,text2,i+1,j+1))


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        recur = False
        if recur == True:
        #recursion
            self.i = 0
            self.j = 0
            

            return( self.recursion(text1,text2,self.i,self.j))
        else: #DP
            T = []
            for i in range(len(text1)+1):
                T.append([])
                if i == 0:
                    for j in range(len(text2)+1):
                        T[i].append(0)
                else:
                    T[i].append(0)

            print(T)
            
            for i in range(1,len(text1)+1):
                for j in range(1,len(text2)+1):
                    # print(T[i][j])
                    if text1[i-1] == text2[j-1]:# because text starts from 0 index but T from 1 as 1st row and columns are 0 
                        #T[i].append(1+max(T[i-1][j],T[i-1][j-1],T[i][j-1]))
                        #the above is works but it's not conceptually right
                        # for example if we know text1[i-1] == text2[j-1] then we don't have to do the max 
                        # it should be just adding 1 to T[i-1][j-1]
                        T[i].append(1+ T[i-1][j-1])
                    else :
                        # T[i].append(max(T[i-1][j],T[i-1][j-1],T[i][j-1]))
                        # by same logic, since the current above if is not satisisfied that means we dont need T[i-1][j-1]
                        # we only can go to T[i-1][j],T[i][j-1]
                        T[i].append(max(T[i-1][j],T[i][j-1]))
            
            return T[-1][-1]



        

        