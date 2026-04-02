class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        cnt = 0
        while l<=r:
            m = l+(r-l)//2
            print(l,m,r,'---')
            print(nums[l],nums[m],nums[r],'+++')
            if nums[m] == target:
                return m
            elif nums[m]>=nums[l] :
                if  nums[l]<=target<= nums[m]:
                    r= m-1
                else:
                    l = m+1
            elif nums[m]<nums[l]:
                if  nums[m]<=target<= nums[r]:
                    l = m+1
                else:
                    r = m-1
            cnt+=1

        return -1

