class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1
        m = l+(r-l)//2
        print(m, nums[m])
        if len(nums)<3:
            return min(nums)
        while nums[m-1]<nums[m] <nums[m+1]:
            print('----1----')
            if nums[l]<nums[m]<nums[r]:
                r= m-1
            elif nums[l]< nums[m] and nums[r] <nums[m]:
                if nums[l]<nums[r]:
                    r = m-1
                else:
                    l = m+1
            elif nums[l]> nums[m] and nums[r] >nums[m]:
                if nums[l]>nums[r]:
                    r = m-1
                else:
                    l = m+1
            elif nums[l]>nums[m]>nums[r]:
                l = m+1
            m = l+(r-l)//2
        return min(nums[m-1],nums[m] ,nums[m+1])