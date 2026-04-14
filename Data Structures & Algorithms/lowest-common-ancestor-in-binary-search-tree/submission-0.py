# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def getparents(root, node,parent_list):
            if not root:
                return False 
            # print(root.val,node.val)
            # parent_list.append(root)
            # print(root.val,self.v)
            if root.val == node.val :
                # print("yay",root.val,node.val)
                parent_list.append(root)
                self.v = True
                return True
            parent_list.append(root)
            
            if not self.v  :
                if  root.val >  node.val:
                    getparents(root.left, node,parent_list)
                if  root.val <  node.val:
                    getparents(root.right,node,parent_list)
            # parent_list.append(root.val)
            # return max(getparents(root.left, node,parent_list), getparents(root.right,node,parent_list))
            
            # if not getparents(root.left, node):
            #     getparents(root.right,node)
            # if not getparents(root.right,node):
            #     getparents(root.left,node)
        
        # self.parent_list = []
        self.parent_list = []
        self.v = False
        p_list = []
        getparents(root,p,p_list)
        
        print('------------------')
        self.v = False
        q_list = []
        getparents(root,q,q_list)
        # print(p_list,q_list)
        
        for i in p_list:
            print(i.val)

        print('----------')

        for i in q_list:
            print(i.val)
        # return min(self.parent_list)

        for i in range(min(len(p_list),len(q_list))):
            if p_list[i]!= q_list[i]:
                return p_list[i-1]
        if len(p_list)>len(q_list):
            return q_list[-1]
        else:
            return p_list[-1]


        
        