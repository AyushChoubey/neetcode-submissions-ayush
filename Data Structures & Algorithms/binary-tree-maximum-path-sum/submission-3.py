# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root):

                if not root:
                        return float("-inf")

                l = dfs(root.left)
                r = dfs(root.right)
                print(root.val,l,r,max( l+root.val,r+root.val,root.val,l+r+root.val,l,r))
                
                self.max_sum = max(self.max_sum,l+root.val,r+root.val,root.val,l+r+root.val,l,r)
                
                return max( l+root.val,r+root.val,root.val)
        self.max_sum = float("-inf")
        return max(dfs(root),self.max_sum)

 
        