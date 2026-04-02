class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def recursion(nums,value,i):
            if  i == len(nums):
                if value == target:
        
                   return 1
                else :
                   return 0
    
            return((recursion(nums,value+nums[i],i+1) + recursion(nums,value-nums[i],i+1)))


         
        return recursion(nums,0,0)