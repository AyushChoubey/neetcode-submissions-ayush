class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0
        freq_dict = {}
        max_len = []

        while r < len(s):

            if s[r] not in freq_dict:
                freq_dict[s[r]] = 1
            else:
                freq_dict[s[r]] += 1

            # max_key = max(freq_dict, key=freq_dict.get)
            no_rplcmnt = (r-l+1)- max(freq_dict.values())
            print(freq_dict, no_rplcmnt)
            if no_rplcmnt >k:
                
                # r=l
                freq_dict[s[l]]-=1 
                l =l+1
            else:
                max_len.append(r-l+1)
            r=r+1
        return max(max_len)




        