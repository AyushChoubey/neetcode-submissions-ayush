class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        s = sum(nums)
        if s%2 !=0:
            return False

        else:

            target = s//2

        T = [[False]*(target+1) for _ in range(len(nums)+1)]
        
        for i in range(len(nums)+1):
            T[i][0]=True

        
        for i in range(1,len(nums)+1):
            for j in range(1,target+1):

                if j>=nums[i-1]:

                    T[i][j] = T[i-1][j-nums[i-1]] or T[i-1][j]

        # print(T)
        # for i in range(len(nums)+1):
        #     if T[i][-1]==True:
        #         return True
        
        return T[-1][-1]


        