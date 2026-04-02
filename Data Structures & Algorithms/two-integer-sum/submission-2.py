class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_diff  = []
        dict_count = {}
        result = []
        for i in range(len(nums)):
            nums_diff.append(target-nums[i])
            # print(i,len(nums)-i-1)
            # if nums[i]+nums[len(nums)-i-1] == target:
            #     print(i,len(nums)-i-1)
            #     return [i,len(nums)-i-1]
        for i in range(len(nums)):
            if nums[i] not in dict_count.keys():
                dict_count[nums[i]] =1
        for i in range(len(nums)):
            if nums_diff[i] in dict_count.keys()  :
               result.append(i)
            #    if nums_diff[i] != nums[i] and nums[i]*2:

                   
                    
        if len(result)>2:
            
            result.remove(nums.index(target//2))

        return result    