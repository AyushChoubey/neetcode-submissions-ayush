class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s =0
        for i in nums:
            s = i^s
            
        return s