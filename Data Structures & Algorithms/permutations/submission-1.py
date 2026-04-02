class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        
        def get_perm(path,num,nums):
            if len(path) == len(nums):
                print(path)
                self.result.append(path.copy())
            print(path)
            for i in range(len(num)):
                picked = num[i]
                num.pop(i)
                path.append(picked)
                get_perm(path,num,nums)
                path.pop()
                num.insert(i,picked)

        get_perm([],nums.copy(),nums)
        return self.result
