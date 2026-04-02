class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        freq_dict = {}
        result = []
        while r<n:
            if s[r] not in freq_dict.keys():
                freq_dict[s[r]] = 1
            else:
                freq_dict[s[r]] += 1

            m   = max(freq_dict, key=freq_dict.get)
            rep = r+1-l-freq_dict[m]
            if rep <= k:
                result.append(r-l+1)
            else:
                freq_dict[s[l]]-= 1
                l= l+1
                
            r= r+1
        # print(result)

        return max(result)



            




        