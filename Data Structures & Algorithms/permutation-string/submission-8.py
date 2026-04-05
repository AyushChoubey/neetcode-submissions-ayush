class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l =0 
        r = 0
        if len(s1)>len(s2):
            return False
        freq_dict_s1 = {}
        freq_dict_s2 = {}
        freq_dict_s3 = {}
        for i in s1:
            if i not in freq_dict_s1:
                freq_dict_s1[i] =1
                freq_dict_s2[i] =0
                freq_dict_s3[i] =0
            else:
                freq_dict_s1[i] +=1

        
        
        while r <len(s2):
            if s2[r] in freq_dict_s2:
                freq_dict_s2[s2[r]]+=1

            
            # print(freq_dict_s2,r-l+1,s2[r])
            if r-l+1 == len(s1):
                if freq_dict_s2  == freq_dict_s1:
                    return True
                else:
                    # if s2[l] in freq_dict_s2:
                    #     freq_dict_s2[s2[l]]-=1
                    # l=+1
                    r=l
                    l=l+1
                        
                    freq_dict_s2 = freq_dict_s3.copy()
            r=r+1
        
        # print(freq_dict_s2)
        return False 


            
        