class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(0,n+1):
            c = 0
            for j in range(i):
                if 1<<j & i:
                    c+=1
            res.append(c)
        return res
            


