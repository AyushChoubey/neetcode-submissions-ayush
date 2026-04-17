# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q =[]
        res = []
        if root:
            q.append(root)
        else:
            return []

        while q:
            # print(res,q)
            l = len(q)
            # qu=[]
            # for i in range(l):
            #     qu.append(q[i].val)
            # print(res,qu)
            # print(l)
            for i in range(l):
                # print(res,q[i].val)
                n = q.pop(0)
                if n :
                    if i ==l-1:
                        res.append(n.val)
                    # qu.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            # print(qu)
        return res



        