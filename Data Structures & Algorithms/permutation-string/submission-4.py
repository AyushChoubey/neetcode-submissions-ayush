class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)-1
        dict_s1 = {}
        if len(s1)>len(s2):
            return False

        for i in s1:
            if i not in dict_s1.keys():
                dict_s1[i] = [1,0]
            else:
                dict_s1[i][0]+=1
        
        for i in range(len(s1)):
            if s2[i] in dict_s1.keys():
                dict_s1[s2[i]][1]+=1
        

        while r<len(s2)-1:
            print(dict_s1)
            s = True
            for i in dict_s1:
                if dict_s1[i][0] !=dict_s1[i][1]:
                    s = False 
            if s==True :
                return True
            if  s2[l] in dict_s1.keys():
                dict_s1[s2[l]][1]-= 1
            l = l+1
            r = r+1
            # print(s2[r])

            if  s2[r] in dict_s1.keys():
                dict_s1[s2[r]][1]+= 1
        s = True
        for i in dict_s1:
            if dict_s1[i][0] != dict_s1[i][1]:
                s = False
        if s:
            return True
        return False 



        