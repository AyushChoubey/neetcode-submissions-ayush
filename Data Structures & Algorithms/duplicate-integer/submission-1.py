class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_ = {}

        for i in nums:
            if i not in dict_:
                dict_[i] =1
            else:
                return True
        return False
        