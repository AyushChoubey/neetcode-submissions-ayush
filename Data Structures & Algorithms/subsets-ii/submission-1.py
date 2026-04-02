class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result =[]
        nums.sort()

        def dfs(i,nums,path):
            if i == len(nums):
                self.result.append(path.copy())
                return
                
            path.append(nums[i])
            dfs(i+1,nums,path)
            path.pop()

            while i+1<len(nums) and nums[i] == nums[i+1]:
                i = i+1
            dfs(i+1,nums,path)

        dfs(0,nums,[])
        return self.result