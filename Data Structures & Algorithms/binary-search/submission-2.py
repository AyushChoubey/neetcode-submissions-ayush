class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # def bsearch(nums,target,pos):
        #     print(len(nums),nums)
        #     if len(nums) == 1:
        #         # print('yess')
        #         if nums[0] == target :
        #             return 0
        #         else :
        #             # print('yesss')
        #             return -1
        #     if nums[len(nums)//2] > target:
        #        return bsearch(nums[0:len(nums)//2],target,pos)
        #     elif nums[len(nums)//2] < target:
        #        pos = pos+len(nums)//2
        #        return bsearch(nums[len(nums)//2:],target,pos)
        #     else:
        #         if pos>0:
        #             return pos+ len(nums)//2
        #         else:
        #             return len(nums)//2
        # return bsearch(nums,target,0)

        # The above solution is recursion based solution it's not optimal to write this much instead
        # we can write is using a while loop
        i = 0 
        j = len(nums)-1
        k = 0
        while i<=j:
            # print(i,j,i+(j-1)//2)
            if nums[i+(j-i)//2]> target:
                j = i+(j-i)//2-1
            elif nums[i+(j-i)//2]< target:
                i = i+(j-i)//2+1
            else: return i+(j-i)//2
            # k=k+1
        
        return -1


            
        