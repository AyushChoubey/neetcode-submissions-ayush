class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        T = [[False]*n for _ in range(n)]
        count = 0

        for i in range(n):
            T[i][i] = True
            count+=1
        


        for l in range(2,n+1):
            for i in range(n-l+1):
                j = l+i-1
                
                if l==2:
                    if s[i] == s[j]:
                        T[i][j] = True
                        count+=1
                        # print("2")
                else:
                   
                    T[i][j]  = (s[i] == s[j] and T[i+1][j-1])
                    
                    if T[i][j] == True:
                        count+=1
                        # print("3")
        
        # print(T)
        return count
            
        