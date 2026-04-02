class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[-1]
        T1 = [0]*(len(nums))
        T1[0] = 0
        T1[1] =  nums[0]
        # track_dict = {}

        #subproblem def : maximum amount at ith house = maximum(nums[i]+T[i-2],T[i-1])
        # print(T)
        for i in range(2, len(nums)):
            # if i != len(nums):
                T1[i] = max(nums[i-1]+T1[i-2],T1[i-1])
                 

            # else:
            #     T1[i] = max(nums[i-1]+T1[i-2]-nums[0],T1[i-1])
            #     print(nums[i-1]+T1[i-2]-nums[0],T1[i-1])
        nums2 = nums[::-1]
        T2 = [0]*(len(nums))
        T2[0] = 0
        T2[1] =  nums2[0]
        # track_dict = {}

        #subproblem def : maximum amount at ith house = maximum(nums[i]+T[i-2],T[i-1])
        
        for i in range(2, len(nums)):
            # if i != len(nums):
                T2[i] = max(nums2[i-1]+T2[i-2],T2[i-1])
                 

            # else:
            #     T2[i] = max(nums[i-1]+T2[i-2]-nums[0],T2[i-1])
            #     print(nums[i-1]+T1[i-2]-nums[0],T2[i-1])

        
        print(T1,T2)
        return max(T1[-1],T2[-1])