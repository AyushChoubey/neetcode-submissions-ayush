# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         self.result = []
#         self.visited = []
#         def comb(nums, path, current_sum,target):
#              if current_sum >= target:
#                 if current_sum == target:
#                     # if sorted(path.copy() ) not in self.result:
#                     self.result.append(path.copy())
#                 return
#              for i in range(len(nums)):
#                 picked = nums[i]
#                 print(path,nums)
#                 if picked not in self.visited:
#                     path.append(picked)
#                     nums.pop(i)
#                     self.visited.append(picked)
                
#                     current_sum += picked

#                     comb(nums[i:],path, current_sum,target)
#                     current_sum -=picked
#                     path.pop(-1)
#                     nums.insert(i,picked)
#                     self.visited.pop()

                
        

#         comb(candidates,[],0,target)
        
#         return self.result





class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        # self.visited = []
        def comb(nums, path, current_sum,target,visited):
             if current_sum >= target:
                if current_sum == target:
                    # if sorted(path.copy() ) not in self.result:
                    self.result.append(path.copy())
                return
             for i in range(len(nums)):
                picked = nums[i]
                print(path,nums,visited)
                if picked not in visited:
                    path.append(picked)
                    nums.pop(i)
                    visited.append(picked)
                    
                    current_sum += picked

                    comb(nums[i:],path, current_sum,target,[])
                    current_sum -=picked
                    path.pop(-1)
                    nums.insert(i,picked)
                # self.visited.pop()

                
        
        candidates.sort()
        
        comb(candidates,[],0,target,[])
        
        return self.result

    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     self.result = []
    #     def comb(nums, path, current_sum,target):
    #             if current_sum >= target:
    #                 if current_sum == target:
    #                     # if sorted(path.copy() ) not in self.result:
    #                     self.result.append(path.copy())
    #                 return
    #             for i in range(len(nums)):
    #                 picked = nums[i]
    #                 path.append(picked)
    #                 current_sum += picked
    #                 comb(nums[i+1:],path, current_sum,target)
    #                 current_sum -=picked
    #                 path.pop(-1)
            

    #     comb(candidates,[],0,target)
        
    #     return self.result
        