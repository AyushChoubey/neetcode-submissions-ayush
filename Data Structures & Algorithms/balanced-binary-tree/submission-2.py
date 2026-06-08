# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.check_list =[]
        def check_balanced(root):

            if not root:
                return 0
            

            l = check_balanced(root.left)
            r = check_balanced(root.right)
            print(root.val,l,r)

            if abs(l-r) >1:
                self.check_list.append(False)
            else:
                self.check_list.append(True)
            return 1+max(l,r)

        check_balanced(root)
        # print(self.check_list)
        if sum(self.check_list) == len(self.check_list):
            return True
        else:
            return False

    



            
        