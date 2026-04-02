class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l = 0
        r= len(heights)-1
        while l < r:
            area = (r-l)*min(heights[r],heights[l])
            # print(area,(r-l),min(heights[r],heights[l]))
            if area >max_area:
                max_area = area
            if heights[r] >heights[l]:
                l=l+1
            elif heights[l]>heights[r]:
                r = r-1
            else:
                r= r-1
                l=l+1

        return max_area
            
        