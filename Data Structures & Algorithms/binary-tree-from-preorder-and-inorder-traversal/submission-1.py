# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # the starting element of the preorder gives us the root 
        # then if we search that elemnt in inorder the all the elements before that element will be in the left  subtree 
        # and the and all the elements to the right will be in the right subtree  

        def add_node(preorder, inorder):

                if inorder ==[] or preorder ==[]:
                        
                        return
                
                split = inorder.index(preorder[0])
                root =  TreeNode(preorder[0])
                # print(split,root.val,inorder,preorder)
                
                # print(split,root.val,inorder,preorder)
                
                root.left = add_node(preorder[1:split+1], inorder[:split])
                root.right = add_node(preorder[split+1:], inorder[split+1:])
                return root
        
        return add_node(preorder,inorder)
        

                


        