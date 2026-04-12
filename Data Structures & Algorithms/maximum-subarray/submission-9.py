class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        T= [0]*(len(nums)+1)
        T[0] = float("-inf")
        for i in range(1,len(nums)+1):
            T[i] = max(nums[i-1]+T[i-1],nums[i-1])
        
        # print(T)
        return max(T)
