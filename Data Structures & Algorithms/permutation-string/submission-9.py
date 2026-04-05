class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l =0 
        r = 0
        if len(s1)>len(s2):
            return False
        freq_dict_s1 = {}
        freq_dict_s2 = {}
        
        for i in s1:
            if i not in freq_dict_s1:
                freq_dict_s1[i] =1
                freq_dict_s2[i] =0
            else:
                freq_dict_s1[i] +=1

        
        
        while r <len(s2):
            if s2[r] in freq_dict_s2:
                freq_dict_s2[s2[r]]+=1
            
            if r-l+1 > len(s1):
                if s2[l] in freq_dict_s2:
                    freq_dict_s2[s2[l]]-=1
                l=l+1


            
            
            
            
            if freq_dict_s2  == freq_dict_s1:
                return True
               
            r=r+1
        
        return False 


            
        