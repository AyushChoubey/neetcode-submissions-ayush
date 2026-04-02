class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}

        for i in nums:
            if i not in count_dict.keys():
                 count_dict[i] = 1
            else:
                count_dict[i]+=1

            if count_dict[i] >1:
                return True
        
        return False
        
        