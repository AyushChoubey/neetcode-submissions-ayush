class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        print(nums)
        
        for i in range(len(nums)):
            # print(i)
            l= 0 
            r = len(nums)-1
            t = -(nums[i])
            # c=0
            while l<r :
                if i==l :
                    l=l+1
                    continue
                if i==r:
                    r= r-1
                    continue
                # print(nums[i],nums[l],nums[r],i,l,r,result)
                if nums[l]+nums[r] == t :
                    s_r = sorted([nums[i],nums[l],nums[r]])
                    if s_r not in result:
                        result.append(s_r)
                    r = r-1
                    l = l+1
                    
                else:
                    if nums[l]+nums[r]> t :
                        r = r-1
                    if nums[l]+nums[r]< t :
                        l = l+1
                # c=c+1
            


    
        return result 



        