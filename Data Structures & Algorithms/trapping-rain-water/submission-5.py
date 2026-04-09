class Solution:
    def trap(self, height: List[int]) -> int:

        left_max = []
        right_max = []

        stack = []
        for i in range(len(height)):
            if stack ==[] or stack[-1]<height[i]:
                if stack ==[]:
                    left_max.append(height[i])
                    stack.append(height[i])
                else:
                    stack.pop()
                    
                    stack.append(height[i])
                    left_max.append(stack[-1])
            else:
                left_max.append(stack[-1])
        

        # print(left_max)
        stack =[]
        for i in range(len(height)-1,-1,-1):
            if stack ==[] or stack[-1]<height[i]:
                if stack ==[]:
                    right_max.append(height[i])
                    stack.append(height[i])
                else:
                    stack.pop()
                    
                    stack.append(height[i])
                    right_max.append(stack[-1])
            else:
                right_max.append(stack[-1])
            
        
        right_max = right_max[::-1]
        # print(right_max)
        area = 0

        for i in range(len(height)):
            area+= min(left_max[i],right_max[i])-height[i]
        return area
            
        