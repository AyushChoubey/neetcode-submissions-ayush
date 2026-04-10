import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
      
        heapq.heapify(nums)
        self.nums = nums
        # print(self.nums)
        
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        # print(self.nums)
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
            
        # print(self.nums)
        
        return (self.nums[0])

        
