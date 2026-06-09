class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        T= [[0]*(len(nums)+1) for i in range (2)]
        T[0][0] =1
        T[1][0] =1
        
        for i in range(1,len(nums)+1):

            T[0][i]  = max(T[0][i-1]*nums[i-1],T[1][i-1]*nums[i-1],nums[i-1])
            T[1][i] = min(T[0][i-1]*nums[i-1],T[1][i-1]*nums[i-1],nums[i-1])


        
        # T2= [0]*(len(nums)+1)
        # T2[0] =1
        # for i in range(1,len(nums)+1):
        #     T2[i] = min(T2[i-1]*nums[i-1],nums[i-1])

            

        print(T)
        
        return max(T[0][1:])

        