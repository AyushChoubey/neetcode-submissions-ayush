class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_bound = []
        right_bound = []
        stack = []
        for i in range(len(heights)):
            # print(stack,left_bound, i)

    

            if stack ==[]  or stack[-1][0]<heights[i]:
                if stack ==[] :
                    left_bound.append(0)
                    stack.append((heights[i],i))
               
                else :
                    left_bound.append(i)
                    stack.append((heights[i],i))
            else:
                
                while stack !=[] and stack[-1][0]>=heights[i]:
                    stack.pop()
                if stack ==[] :
                    left_bound.append(0)
                    stack.append((heights[i],i))
               
                else :
                    left_bound.append(stack[-1][1]+1)
                    stack.append((heights[i],i))
        # print(stack)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            # print(stack,right_bound, i)
            
            if stack ==[]  or stack[-1][0]<heights[i]:
                if stack ==[] :
                    right_bound.append(len(heights)-1)
                    stack.append((heights[i],i))
               
                else :
                    right_bound.append(i)
                    stack.append((heights[i],i))
            else:
                
                while stack !=[] and stack[-1][0]>=heights[i]:
                    stack.pop()
                if stack ==[] :
                    right_bound.append(len(heights)-1)
                    stack.append((heights[i],i))
               
                else :
                    right_bound.append(stack[-1][1]-1)
                    stack.append((heights[i],i))
        right_bound = right_bound[::-1]

        area=[]
        for i in range(len(heights)):
            # width = right_bound[i]-left_bound[i]
            width = right_bound[i] - left_bound[i] + 1
            # if width !=0:
            area.append(width*heights[i])
            # else:
            #     area.append(heights[i])


        # print(left_bound, right_bound, area)
        return max(area)
        


            

