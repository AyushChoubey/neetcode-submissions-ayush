class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.result = []

        def get_combination(nums,path,target):

            if target<=0:
                if target==0:
                    self.result.append(path.copy())
                return
            

            for i in range(len(nums)):
                picked = nums[i]
                path.append(picked)
                target -= picked
                get_combination(nums[i:],path,target)
                path.pop()
                target+= picked
            


        get_combination(nums,[],target)
        return self.result            
            
