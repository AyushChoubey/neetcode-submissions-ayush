class Solution:
    def hammingWeight(self, n: int) -> int:
        s = 0
        for i in range(32):
            a = (1 << i)
            if a & n == a:
                s+=1

        return s
        