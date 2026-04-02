class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        r = len(s1)-1

        s1_s = sorted(s1)
        n = len(s2)
        while r<n:
            if  sorted(s2[l:r+1]) == s1_s:
                return True
            else:
                r = r+1
                l = l+1
        return False

        