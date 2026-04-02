class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        min_len = float("inf")
        result = ""
        dict_n = {}
        dict_h = {}
        for i in t:
            if i not in dict_n.keys():
                dict_n[i] = 1
            else:
                dict_n[i]+=1
        cnt = len(dict_n)
        for i in t:
            if i not in dict_h.keys():
                dict_h[i] = 0


        while r<len(s):

            if s[r] in dict_h.keys():
                dict_h[s[r]] += 1
                if dict_n[s[r]] - dict_h[s[r]] ==0:
                    cnt -= 1

            if cnt==0:
                while cnt == 0:
                    if (r+1-l)< min_len:

                        result  = s[l:r+1]
                        min_len = (r+1-l)
                    
                    if s[l] in dict_h.keys():
                        dict_h[s[l]] -= 1
                        if dict_h[s[l]] < dict_n[s[l]]: #dict_n[s[l]] - dict_h[s[l]] ==0:
                            cnt += 1
                    l = l+1
                # if (r+1-l-1)< min_len:

                #     result  = s[l-1:r+1]
                #     min_len = (r-l-1)
                
                  

            r= r+1

        return result 

            


        