# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def identical(p,q):
            
            if not p or not q:
                if not p and not q:
                    return True
                else:
                  
                    return  False
            # print(root.val, subroot.val,'--------')
            if p.val==q.val and identical(p.left,q.left) and identical(p.right,q.right):
                return True
            else:
                return False
        
       





        def findroot(root,subRoot):
            
            if not root  :
                return False
            
            if root.val == subRoot.val:
                return identical(root,subRoot) or findroot(root.left,subRoot) or findroot(root.right,subRoot)
            else:
                return findroot(root.left,subRoot) or  findroot(root.right,subRoot)

            
        return findroot(root,subRoot)
        # new_root = findroot(root,subRoot)  
        # # print(new_root.val ,'new_root')
        # if new_root:
           
        #     return traversal(new_root,subRoot)
        # else:
        #     return False
    
        


                