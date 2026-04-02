class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        end = len(nums)
        nums.sort()
        

        def get_subset(path,nums):
            # if len(path) == end:
            #     self.result.append(path.copy())
            #     return
            #since nums is already  getting smaller and smaller we it will auto terminate so we don't need any 
            self.result.append(path.copy())
            # print(path)
            visited = []
            # print(visited)
            for i in range(len(nums)):
                   
                    picked = nums[i]
                    if picked not in visited:
                        path.append(picked)
                        visited.append(picked)
                        # nums.pop(i)
                        get_subset(path,nums[i+1:])
                        path.pop()
                        # visited.pop()
                        # nums.insert(i,picked)


        get_subset([],nums)
        return self.result