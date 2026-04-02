class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        def get_comb_sum(path,current_sum,target,nums):
            if current_sum >= target:
                if current_sum == target:
                    # print(path)
                    self.result.append(path.copy())
                return
            # print(path)
            for i in range(len(nums)):
                picked = nums[i]
                path.append(picked)
                current_sum += picked
                get_comb_sum(path,current_sum,target,nums[i:])
                current_sum -= picked
                path.pop()
        get_comb_sum([],0,target,nums)
        return self.result