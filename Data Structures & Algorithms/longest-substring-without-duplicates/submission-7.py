class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        pos_dict = {}

        l = 0
        r = 0
        cur_len = 0

        while r!= len(s):
            # print(l,r,cur_len,max_len)

            if s[r] not in pos_dict:
                pos_dict[s[r]] = r
                cur_len +=1

                max_len = max(max_len,cur_len)
                

            else:
                i = l 
                l = pos_dict[s[r]]+1
                # print(pos_dict,l,i,r)
                while i !=l:
                   del pos_dict[s[i]]
                   i+=1
                pos_dict[s[r]] = r

                cur_len = r-l+1
            
            r+=1
        
        return max_len





