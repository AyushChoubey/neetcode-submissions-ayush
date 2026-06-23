class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        max_len = 0

        for i in num_set:
            if i-1 not in num_set:
                curr_len = 1
                while i+1 in num_set:
                    curr_len +=1
                    i+=1

                max_len = max(curr_len,max_len)

        return max_len



        