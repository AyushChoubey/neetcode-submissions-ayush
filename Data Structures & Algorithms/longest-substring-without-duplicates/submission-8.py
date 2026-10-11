class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        pos_dict = {}

        l = 0
        r = 0
        cur_len = 0
        res = 0

        while r!= len(s):
            # print(l,r,cur_len,max_len)

            if s[r] in pos_dict:

                l = max(l,pos_dict[s[r]]+1)
            pos_dict[s[r]] = r

            res = max(res, r-l+1)

            r+=1






            
        
        return res





