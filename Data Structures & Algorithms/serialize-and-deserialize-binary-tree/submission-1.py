# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # lets try to create preorder and inorder and combine themas we have seen if we have those two we can create the tree 

        def preorder(root):
                if not root:
                        self.pre.append("N")

                        return 
                
                self.pre.append(str(root.val))
                preorder(root.left)
                # self.pre.append('L')
                

                preorder(root.right)
                # self.pre.append('R')
        self.pre = []

        preorder(root)

        return ",".join(self.pre)


        


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '':
                return 
        # print(data)

        self.data = [i for i in data.split(',')]


        def maketree():
                if self.data[0] == 'N' :
                        self.data.pop(0)
                        return
              
                
                root = TreeNode(int(self.data[0]))
                self.data.pop(0)
                # print(root.val,self.data)
                root.left = maketree()
                # print(root.val,self.data)
                root.right = maketree()

                return root
        
        
        return maketree()
        
        


                

