class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.l = len(nums)
        self.result =[]
        
        def get_per(nums,path):
            if len(path) == self.l:
                self.result.append(path.copy())
            
            for i in range(len(nums)):
                c_i = nums.pop(i)
                path.append(c_i)

                get_per(nums,path)
                nums.insert(i,c_i)
                path.pop()
        
        get_per(nums,[])
        return self.result 



