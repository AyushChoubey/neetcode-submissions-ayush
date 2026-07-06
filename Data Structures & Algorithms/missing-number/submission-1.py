class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0

        for i in range(len(nums)):
            sum+= nums[i]
        real_sum = ((len(nums)+1)*len(nums))//2 
        print(real_sum,sum)
        if real_sum != sum:
            return real_sum - sum
        else:
            return 0

                
            
        