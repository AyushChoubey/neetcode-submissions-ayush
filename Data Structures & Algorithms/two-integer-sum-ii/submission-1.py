class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r= len(numbers)-1

        while r>l:
            if numbers[r]+numbers[l]==target:
                return [l+1,r+1]
            else:
                if numbers[r]+numbers[l]<target:
                     l = l+1
                if numbers[r]+numbers[l]>target:
                    r = r-1
                   

                
                