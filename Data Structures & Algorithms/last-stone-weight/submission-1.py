import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)


        while len(stones)>1:
            # print(stones)
            max_1 = heapq.heappop(stones)
            max_2 = heapq.heappop(stones)

            if max_1< max_2:
                heapq.heappush(stones,max_1-max_2)
            # print(stones)
        

        if len(stones) ==1 :
            return -stones[0]
        else:
            return 0


        
        