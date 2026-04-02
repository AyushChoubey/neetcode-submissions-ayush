class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1
        m = l+(r-l)//2
        # print(m, nums[m])
        # if len(nums)<3:
        #     return min(nums)
        while l<r:
            print('----1----')
            if nums[m]<nums[r]:
                r= m
            else:
                l = m+1
            m = l+(r-l)//2
        return  nums[l]