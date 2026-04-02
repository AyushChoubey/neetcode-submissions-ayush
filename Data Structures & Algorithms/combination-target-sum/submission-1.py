class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        def comb(nums, path, current_sum,target):
             if current_sum >= target:
                if current_sum == target:
                    # if sorted(path.copy() ) not in self.result:
                    self.result.append(path.copy())
                return
             for i in range(len(nums)):
                picked = nums[i]
                path.append(picked)
                current_sum += picked
                comb(nums[i:],path, current_sum,target)
                current_sum -=picked
                path.pop(-1)
        

        comb(nums,[],0,target)
        
        return self.result
        