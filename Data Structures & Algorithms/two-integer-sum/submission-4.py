class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if  nums[i] not in  d :
                d[nums[i]] = []

            d[nums[i]].append(i)
        result = []
        # print(d)
        for i in range(len(nums)):
            if target - nums[i] in  d:
                # print(d[target- nums[i]], nums[i])
                for j in d[target- nums[i]] :
                    if j !=i:
                        result.append(i)
                        result.append(j)
            if result:
                break
        return result



        
            

