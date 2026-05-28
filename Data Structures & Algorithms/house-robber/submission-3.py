class Solution:
    def rob(self, nums: List[int]) -> int:
        
        T= [0]*(len(nums)+2)

        for i in range(2,len(nums)+2):
            T[i] = max(T[i-2]+nums[i-2],T[i-1])

        return T[-1]
