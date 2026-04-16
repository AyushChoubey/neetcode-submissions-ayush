# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        q.append(root)
        if not root: 
            return [] 
        
        result = []
        result.append([root.val])

        while q!=[]:
            
        
            print(q)
            r = []
            v = []
            for root in q:
                print(root.val)
                if root.left :
                    r.append(root.left)
                    v.append(root.left.val)

                if  root.right:
                    
                    r.append(root.right)
                    
                    v.append(root.right.val)
            print(v)
            if v !=[]:
                result.append(v)
            q = r.copy()
        print(result)
        
        return result 
            
            
            
            
