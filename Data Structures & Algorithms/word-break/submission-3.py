class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        T = [False]*(len(s)+1)
        T[0] = True
        i = 1
        i = 1

        index_list = []
        index_list.append(0)
        # while r<len(s)+1:
            
        #     for i in index_list:
        #         if s[l-1:r] in wordDict and T[i]:
                    
        #             T[r]  = True

        #             l = r+1
        #     r=r+1

        # print(T)
        # return T[-1]

        for i in range(1,len(s)+1):
            b = False
            for j in range (0,i):
                # print(s[j-1:i],T[j-1],i,j-1)
                if  T[j] and (s[j:i] in wordDict):
                    b = True
                    break  
            T[i] = b

        # print(T)

        return T[-1]   
            



