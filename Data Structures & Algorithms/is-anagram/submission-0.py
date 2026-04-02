class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        char_dict_s ={}
        char_dict_t ={}
        for i in s:
            if i not in char_dict_s.keys():
                char_dict_s[i] = 1
            char_dict_s[i]+=1
        
        for i in t:
            if i not in char_dict_t.keys():
                char_dict_t[i] = 1
            char_dict_t[i]+=1

        if char_dict_s == char_dict_t:
            return True
        else: return False 
