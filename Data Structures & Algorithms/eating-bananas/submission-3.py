import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_ = max(piles)
        min_ = min(piles)
        # rates = [i for i in range(1,max_+1)]
        l = 1
        r = max_
        min_rate = float("inf")
        while l<=r:
            m = l+(r-l)//2
            s = 0
            # print(rates[m])
            for i in piles:
                
                s= s+ math.ceil(i/m)
            # print(s,h, '----')
            if s > h:
                l= m+1
            elif s<=h:
                if m<min_rate:
                   min_rate = m
                r=m-1
            # else:

            #     min_rate = rates[m]
            #     break


        return min_rate

        