class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =''.join(ch.lower() for ch in s if ch.isalnum())
        i = 0
        j = len(s)-1
        # print(s)
        while i!=len(s)//2:
            # print(s[i],s[j],i,j)

            if (s[i] != s[j]):
                return False

            i+=1
            j-=1

        return True
