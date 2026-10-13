class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        need ={}
        have = {}
        for i in s1:
            if i not in need:
                have[i] = 0
                need[i] = 0
            need[i]+=1
        
        l = 0
        r= len(s1)-1
        print(have, need)
        for i in s2[:len(s1)]:
            if i in have:

                have[i] +=1
        if have == need:
            return True

            

        while r != len(s2)-1:
            if s2[l] in have:
                have[s2[l]] -=1
            l+=1
            r+=1
            if s2[r] in have:
                have[s2[r]]+=1

            if need == have:
                return True
        return False


            
        