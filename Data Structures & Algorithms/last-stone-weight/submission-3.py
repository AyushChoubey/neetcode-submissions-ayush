import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heavy_stones = [-i for i in stones]
        heapq.heapify(heavy_stones)

        while len(heavy_stones)>1:
            x = heapq.heappop(heavy_stones)
            y = heapq.heappop(heavy_stones)
            if x !=y:
                heapq.heappush(heavy_stones,x-y)
        

        if len(heavy_stones) ==1 :
            return -heavy_stones[0]
        else:
            return 0

            
            
        