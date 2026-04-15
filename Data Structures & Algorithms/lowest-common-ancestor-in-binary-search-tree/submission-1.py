# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if p.val>root.val and q.val>root.val:
            # if both are greater than node they must be in right of the node
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val<root.val and q.val<root.val:
             # if both are smaller than node they must be in left of the node 
            return self.lowestCommonAncestor(root.left, p, q)
        
        
        return root
        

        