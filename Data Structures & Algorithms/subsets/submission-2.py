class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        end = len(nums)

        def get_subset(path,nums,end):
            if len(path) == end:
                self.result.append(path.copy())
                return
            self.result.append(path.copy())
            # print(path)
            for i in range(len(nums)):
                picked = nums[i]
                path.append(picked)

                get_subset(path,nums[i+1:],end)
                path.pop()


        get_subset([],nums,end)
        return self.result
        