class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

      

        l = 0 
        r  = 0
        char_dict = {}
        max_len = 0


        while r < len(s):
           
            if s[r] not in char_dict:
                char_dict[s[r]] = 0
            char_dict[s[r]] += 1
            
            if (r-l+1)-max(char_dict.values())>k:
                
                char_dict[s[l]] -= 1
                l = l+1
            else:
                # max_len = max(r-l+1,max_len)
                if r-l+1>max_len:
                    max_len = r-l+1

            r+=1

        return max_len
            

                
            

            

        