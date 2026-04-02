# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bt(root):
            if not root:
                return 0 

            l = bt(root.left)
            r = bt(root.right)
            self.l.append(abs(l-r))
            return 1+max(l,r)

        self.l =[]   
        bt(root)

        for i in self.l:
            if i >1:
                return False
        return True
        # print(bt(root.left),bt(root.right))  
        # if not root:
        #     return True
        # if abs(bt(root.left)-bt(root.right))>1:
        #      return False
        # else:
        #     return True
        

            
         