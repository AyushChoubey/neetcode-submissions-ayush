class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # l = 0
        # r = len(nums)-1
        # result = []
        # while l<r:
        #     for k in nums[l+1:r]:
        #         print(l,r,k,nums[l],nums[r])
        #         if k+nums[l]+nums[r]==0:
        #             # if [nums[l],k,nums[r]] not in result:
        #             result.append([nums[l],k,nums[r]])
        #             break
        #     if nums[l]+nums[r] >0:
        #             r-=1

        #     else :
        #         l+=1
        
        # return result

        nums.sort()
        result = []
        for i in range(len(nums)):
            l = i+1
            r= len(nums)-1

            t = -(nums[i])
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                
                if nums[l]+nums[r] == t:
                    result.append([nums[i],nums[l],nums[r]])
                    r=r-1
                    l=l+1
                    while nums[l]==nums[l-1] and l<r:
                        l=l+1
                    while nums[r]==nums[r+1] and l<r:
                        r=r-1
                    
                    
                    
                                
                elif nums[l]+nums[r] > t:
                        r=r-1
                else:
                         l=l+1
        return result 

                     


        