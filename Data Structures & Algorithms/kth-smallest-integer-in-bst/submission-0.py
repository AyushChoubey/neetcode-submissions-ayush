# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # the smallest number will be at left extreme of the tree then second will be it's parent and then next be the right of it 
        # we can try DFS on this one 

        def dfs(root):
            if not root:
                return 
            
            
            dfs(root.left)
            
            self.k=self.k-1
            if self.k ==0:
                self.res = root.val
            # print(root.val,self.k)
           
            dfs(root.right)
           
            
        
        self.k = k
        self.res = None
        dfs(root)
        print(self.res)
        return self.res
            

        