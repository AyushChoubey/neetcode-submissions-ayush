# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
                if not node: return 0          # ← 0 not -inf!
                l = max(dfs(node.left),  0)    # ignore negative paths
                r = max(dfs(node.right), 0)    # ignore negative paths
                self.max_sum = max(self.max_sum, l + r + node.val)
                return node.val + max(l, r)    # return best single path up
        self.max_sum = float("-inf")

        dfs(root)
        return self.max_sum

 
        