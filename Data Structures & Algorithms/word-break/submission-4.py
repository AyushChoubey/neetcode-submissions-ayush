class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # the other way is to match every word in the dict
        T = [False]*(len(s)+1)
        T[-1] = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if i+len(w)<=len(s) and s[i:i+len(w)] == w:
                    T[i] = T[i+len(w)]
                if T[i] == True:
                    break
            
    
        return T[0]