class Solution:
    def longestPalindrome(self, s: str) -> str:
        T= [[False]*(len(s)) for _ in range(len(s))]
         

        max_cord = (0,0)
        s_r = s[::-1]
        max_len, idx = 0,-1
        for i in range(len(s)):
            T[i][i] = True
            max_len =1 
            idx = i
                    
                    
                        


        for l  in range(1,len(s)+1):
            for i in range(len(s)-l+1):
                j = i+l-1
                # print(i,j)
                # if s[i-1] == s_r[len(s)-1 -(j-1)]:
                #     T[i][j] = 1+T[i-1][j-1]
                
                # max_i, max_j = max_cord
                # if T[i][j] > T[max_i][max_j]:
                #     max_cord = (i,j)

                
                

                if j == i+1:
                    if s[i] == s[j]:
                        T[i][j] = True
                        
                        max_len =2
                        idx = i
                # print(i,j,T[j][i])
                if 0<=j-1<len(s) and 0<=i+1<len(s)  and s[i] == s[j] and T[i+1][j-1]:
                    # print('yess')
                    T[i][j] = True

                    if max_len <l:
                        max_len =l
                        idx = i

                

        # print(T)
            
        return s[idx:idx+max_len]

                

        # print(T,max_cord)

        # i , j = max_cord[0]-1,max_cord[1]-1
        # res = ''
        # print(s[i],s_r[j],i,j)
        # while T[i+1][j+1]!=0 and 0<=i<= len(s)-1 and  0<=j<= len(s)-1:
        #     res= res+s[i]
        #     print(i,j,s[i])
        #     i -=1
        #     j-=1
        # return res

                