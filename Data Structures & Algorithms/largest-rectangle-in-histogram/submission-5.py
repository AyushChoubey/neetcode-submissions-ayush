class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_bound = []
        right_bound = []



        for i in range(len(heights)):

            l = i 

            while l>=0:

                if heights[l]<heights[i]:
                    left_bound.append(l+1)
                    break
                if l==0:
                    left_bound.append(l)
                    break
                l-=1

        # print(left_bound)

        for i in range(len(heights)):

            r = i 

            while r<len(heights):

                if heights[r]<heights[i]:
                    right_bound.append(r-1)
                    break
                if r==len(heights)-1:
                    right_bound.append(r)
                    break
                r+=1

        area=[]
        # print(left_bound,right_bound)
        for i in range(len(heights)):
            # width = right_bound[i]-left_bound[i]
            width = right_bound[i] - left_bound[i]+1
            # if width !=0:
            area.append(width*heights[i])
            # else:
            #     area.append(heights[i])


        # print(left_bound, right_bound, area)
        return max(area)
