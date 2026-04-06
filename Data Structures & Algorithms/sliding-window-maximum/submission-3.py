import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = 0
        r = k
        nums = [(-j,i) for i,j in enumerate(nums)]
        heap = nums[0:k]
        heapq.heapify(heap)
        result =[]
        result.append(-heap[0][0])

        while r < len(nums):
            # print(heap,nums[l])
            if heap[0][0] == nums[l][0]:
                heapq.heappop(heap)
                while heap and heap[0][1] <l:
                    heapq.heappop(heap)

            
            # print(heap[0],nums[l])
            heapq.heappush(heap,nums[r])
            result.append(-heap[0][0])
           
            r=r+1
            l=l+1
            
            

        return result





        