class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[-1]

        T1 = [0]*(len(nums)+1)

        for i in range(2,len(nums)+1):
            T1[i] = max(T1[i-2]+nums[i-2],T1[i-1])
        T2 = [0]*(len(nums)+1)
        nums2 = nums[::-1]

        for i in range(2,len(nums)+1):
            T2[i] = max(T2[i-2]+nums2[i-2],T2[i-1])
        
        return max(T1[-1],T2[-1])

        
        