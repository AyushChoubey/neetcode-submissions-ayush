# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dm(root):
            if not root:
                return 0

            l = dm(root.left)
            r = dm(root.right)
            
            self.d_list.append(r+l)
            return 1+max(r,l)
            # return d_list
        self.d_list = []
        dm(root)
        # print(self.d_list)
        return max(self.d_list)