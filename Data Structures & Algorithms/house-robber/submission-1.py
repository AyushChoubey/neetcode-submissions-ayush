class Solution:
    def rob(self, nums: List[int]) -> int:

        T =[]
        T.append(0)
        T.append(0)

        for i in range(2,len(nums)+2):
            T.append(max(nums[i-2]+T[i-2],T[i-1]))


        # print(T)

        return(T[len(nums)+1])
        