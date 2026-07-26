class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp = -1

        for i in range(len(nums)):
            if nums[abs(nums[i])-1] >0: 
                nums[abs(nums[i])-1] *= -1
            else :
                return abs(nums[i])
            



            

        