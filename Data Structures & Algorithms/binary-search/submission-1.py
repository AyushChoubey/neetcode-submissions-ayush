class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bsearch(nums,target,pos):
            print(len(nums),nums)
            if len(nums) == 1:
                print('yess')
                if nums[0] == target :
                    return 0
                else :
                    print('yesss')
                    return -1
            if nums[len(nums)//2] > target:
               return bsearch(nums[0:len(nums)//2],target,pos)
            elif nums[len(nums)//2] < target:
               pos = pos+len(nums)//2
               return bsearch(nums[len(nums)//2:],target,pos)
            else:
                if pos>0:
                    return pos+ len(nums)//2
                else:
                    return len(nums)//2
        return bsearch(nums,target,0)
        