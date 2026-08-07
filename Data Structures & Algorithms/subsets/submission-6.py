class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # self.result = []

        # def getsubset(nums,path):

        #     if len(nums) ==0:
        #         self.result.append(path.copy())
        #         return
             

        #     self.result.append(path.copy())

        #     for i in range(len(nums)):

        #         path.append(nums[i])

        #         getsubset(nums[i+1:],path)
        #         path.pop()
        # getsubset(nums,[])
        # return self.result

        self.result = []
        def get_subset(nums,path):
            if nums == []:
                self.result.append(path.copy())
                return

            self.result.append(path.copy())

            for i in range(len(nums)):
                picked = nums[i]

                path.append(picked)
                get_subset(nums[i+1:],path)
                path.pop(-1)

        

        get_subset(nums,[])

        return self.result






















                




         
        