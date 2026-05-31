class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:



        T= [0]*len(nums)
        
        for i in range(len(nums)):

            max_val = 0

            for j in range(i):
                if nums[j]<nums[i]: 
                    if 1+T[j]> max_val:
                        max_val = T[j]

            

            T[i] = 1+max_val 
        

        print(T)
        return max(T)




            
        