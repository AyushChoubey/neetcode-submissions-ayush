from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()

        q.append(root)

        result = []
        if not root:
            return []
        result.append(root.val)
        while q:
            l = len(q)
            level = []
            for _ in range(l):
               node =  q.popleft()
               if node.left:
                    q.append(node.left)
                    level.append(node.left.val)
               if node.right:
                    q.append(node.right)
                    level.append(node.right.val)
            if level:
                result.append(level[-1])

            

        return result





            



        