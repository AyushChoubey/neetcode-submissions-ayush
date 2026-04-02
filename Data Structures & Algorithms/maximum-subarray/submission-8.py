class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # sum_list = []
        # s = 0
        # for i in nums:
        #     s = s+i
        #     sum_list.append(s)
        
        # min_ = min(sum_list)
        # max_ = max(sum_list)


        # print(sum_list, min_,max_)
        # argmin = sum_list.index(min_)
        # argmax = sum_list.index(max_)
        # max_sum = 0
        # if max_<0 and min_<0 :
        #     return max(nums)

        # if argmin < argmax and min_<0:
        #     for i in range(argmin+1, argmax+1):
        #         max_sum = max_sum+nums[i]
        #     return max_sum
        # else: return max_

   # better approach without using extra space
        j = 0
        current_sum =0
        max_sum = float('-inf')
        f_i = 0
        f_j = 0
        if max(nums)< 0 :
            return max(nums)

        for i in range (len(nums)):
                
                print(current_sum, nums[i])
                current_sum = current_sum+ nums[i]
                print(j,i,current_sum)
                if current_sum> max_sum:
                    f_i = i
                    f_j = j
                    max_sum = current_sum

                print('max_sum = ', max_sum)
                if current_sum <0 and i+1<len(nums) and nums[i]<0:
                    j = i+1
                    current_sum = 0 
        print(f_i, f_j)
        # print(sum(nums[f_j:f_i+1]))
        
        return sum(nums[f_j:f_i+1])

     



        