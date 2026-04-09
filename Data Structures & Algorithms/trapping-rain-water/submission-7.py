class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        area = 0
        right_max = 0
        left_max = 0

        while l <=r:
            
           
            if right_max>= left_max:
                
                left_max = max(left_max,height[l])

                area += left_max - height[l]
                l=l+1
            else :
                print(r)
                right_max = max(right_max,height[r])
                area += right_max - height[r]
                r=r-1




       
        return area
            