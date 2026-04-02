class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        def get_subset(path,nums):

            if nums == []:
                self.result.append(path.copy())
                return
            self.result.append(path.copy())
            for i in range(len(nums)):
                path.append(nums[i])
                

                get_subset(path,nums[i+1:])

                path.pop()


        get_subset([],nums)
        print(self.result)
        return self.result
            

