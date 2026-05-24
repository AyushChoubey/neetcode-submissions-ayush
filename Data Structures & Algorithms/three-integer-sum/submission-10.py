class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for i in range(len(nums)):
            l = 0
            r = len(nums)-1
            target = -(nums[i])

            while l<r:

                if i !=l and i !=r:
                    if nums[l]+nums[r] == target:
                        print([l,i,r])
                        if [nums[l],nums[i],nums[r]] not in result:
                            result.append([nums[l],nums[i],nums[r]])
                        l = l+1
                        r = r-1
                        # while nums[l] == nums[l] and l <r:
                        #     l = l+1

                        
                    elif nums[l]+nums[r] > target:
                        r= r-1
                    else:
                        l = l+1
                else:
                    break
        return result 

                    



        