class Solution:
    def jump(self, nums: List[int]) -> int:
        # reached_from_dict = {}

        # for i in range(len(nums)):
        #     if i not in reached_from_dict:
        #         reached_from_dict[i] = []

            
        dp = [1000]*len(nums)
        dp[0] = 0


        for i in range(len(nums)):
            for j in range(i,nums[i]+i+1):
                # print(j)
                if j < len(nums):
                    dp[j] = min(dp[j],dp[i]+1)
            # print('**********')

        return dp[-1]

