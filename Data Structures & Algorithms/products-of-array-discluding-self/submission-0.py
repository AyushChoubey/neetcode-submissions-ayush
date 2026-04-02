class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix  = [1]*(len(nums)+1)
        sufix = [1]*(len(nums)+1)
        m =1
        for i in range(1,len(prefix)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(len(sufix)-2,0,-1):
            sufix[i] = sufix[i+1]*nums[i]
        # print(prefix,sufix)
        result = []
        for i in range (len(prefix)-1):
            result.append(prefix[i]*sufix[i+1])

        return result 


