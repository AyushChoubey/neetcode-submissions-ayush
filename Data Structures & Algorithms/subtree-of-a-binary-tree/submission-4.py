# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def is_identical(p,q):
            if not p or not q:
                if not p and not q:
                    return True
                else:
                    return False


                
            if p.val == q.val and is_identical(p.left,q.left) and is_identical(p.right,q.right) :
                return True
            else:
                return False


        
        
        def find_subroot(root, subRoot):
            if not root:
                return False
            if is_identical(root,subRoot): #or find_subroot(root.left,subRoot) or find_subroot(root.right,subRoot)
                 return True
            else:
                return find_subroot(root.left,subRoot) or find_subroot(root.right,subRoot)
           
        return find_subroot(root,subRoot)
            
        

        


      
            

            
        