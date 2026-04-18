# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root,max_till_now):
            if not root:
                return 
            
            print(max_till_now,root.val,self.cnt)
            if root.val>= max_till_now:
                self.cnt+=1
                max_till_now = max(max_till_now, root.val)
            
                
            dfs(root.left,max_till_now)
            dfs(root.right,max_till_now)
            # return cnt
    
        self.cnt = 0
        dfs(root,root.val)
        return self.cnt
        
        

            

        






        