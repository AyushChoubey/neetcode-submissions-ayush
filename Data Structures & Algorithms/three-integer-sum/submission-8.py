class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        l = 0
        r = len(nums)-1
        result  = []


        for i in range(len(nums)):
            l = 0
            r = len(nums)-1

            target = -(nums[i])

            while l <r:

                if i != l  and i !=r:
                    if nums[l]+nums[r] == target:
                        if [nums[i],nums[l],nums[r]] not in result:
                            result.append([nums[i],nums[l],nums[r]])
                        r=r-1
                        l=l+1
                    elif nums[l]+nums[r] > target:
                         r =r-1
                    else:
                        l=l+1
                else:
                    break
        

        return result 




             
            

        