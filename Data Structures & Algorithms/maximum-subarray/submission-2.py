class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum_list = []
        s = 0
        for i in nums:
            s = s+i
            sum_list.append(s)
        
        min_ = min(sum_list)
        max_ = max(sum_list)


        print(sum_list, min_,max_)
        argmin = sum_list.index(min_)
        argmax = sum_list.index(max_)
        max_sum = 0
        if max_<0 and min_<0 :
            return max(nums)

        if argmin < argmax and min_<0:
            for i in range(argmin+1, argmax+1):
                max_sum = max_sum+nums[i]
            return max_sum
        else: return max_


        