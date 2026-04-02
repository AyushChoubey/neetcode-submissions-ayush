# class Solution:
#     def get_subset(self,nums):
#        if nums ==[]:
#         if str(nums[:]) not in self.count_dict.keys():
#             self.count_dict[str(nums[:])] = 1
#             self.result.append(nums[:])
#         return self.result
        
#        for i in range(len(nums)):
#           print(self.result)
#           if str(nums[:]) not in self.count_dict.keys():
#             self.count_dict[str(nums[:])] = 1
#             self.result.append(nums[:])
#         v = nums.pop(i)
#         self.get_subset(nums)
#         nums.insert(i, v)  
          
        

#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         self.result = []
#         self.count_dict = {}
        
       
#         self.get_subset(nums)
#         return self.result

class Solution:
    def get_subset(self, nums, index, path):
        self.result.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.get_subset(nums, i + 1, path)
            path.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.get_subset(nums, 0, [])
        return self.result


        