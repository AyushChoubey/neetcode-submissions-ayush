class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = l+(r-l)//2
            print(nums[l],nums[m],nums[r])
            if nums[l]<= nums[m]:
                if  nums[r]>= nums[m]:
                    return nums[l]
                else:
                    l = m+1
            elif nums[l]>=nums[m]:
                if  nums[r]>= nums[m]:
                    r= m-1
                else:
                    return num[r]
            # print(nums[m-1],nums[m],nums[m+1],"-----")
        
            if nums[m-1]>=nums[m]<=nums[m+1]:
                # print('yay')
                return nums[m]
        return nums[m]