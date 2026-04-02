class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        max_len = 0
        len_ = 0
        dict_  = {}
        j =0
        while j != len(s):
            # print(dict_,i,j,s[j] )
            # print('len_before = ',len_)
            if s[j] in dict_.keys():
                i = dict_[s[j]] + 1
                # del dict_[s[j]] 
                dict_ = {}

                j=i
    
                len_ = 0

            else:
                dict_[s[j]] = j
                len_+=1
                j+=1
            # print('len = ',len_,'max_len = ',max_len)
            if len_>max_len:
                # print(len_,max_len)
                max_len = len_

            
        # print(dict_)
        return max_len

                

            
        