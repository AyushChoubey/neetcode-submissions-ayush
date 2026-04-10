import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist_tup = [(math.sqrt((math.pow(i[0],2))+(math.pow(i[1],2))),[i[0],i[1]]) for i in points]

        heapq.heapify(dist_tup)
        result =[]
        for i  in range(k):
            result.append(heapq.heappop(dist_tup)[1])

        return result