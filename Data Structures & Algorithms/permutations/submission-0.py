class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        def perm(nums,path,new_nums):
            if len(path) == len(nums):
                self.result.append(path.copy())
                return 
            print(path)
            for i in range(len(new_nums)):
                picked = new_nums[i]
                path.append(picked)
                new_nums.pop(i)
                perm(nums,path,new_nums)
                new_nums.insert(i,picked)
                path.pop(-1)
        
        perm(nums,[],nums.copy())

        return self.result
