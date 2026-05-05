class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        
        def get_subset(nums, path):

            self.result.append(path.copy())
            print(path)
            
            for i in range(len(nums)):
                path.append(nums[i])

                get_subset(nums[i+1:],path)

                path.pop()
        get_subset(nums,[])
        return self.result



            
