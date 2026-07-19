"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0,None,None)
        curr = dummy
        ran = dummy
        h = head

        random_map  = {}
        while h:
            
            curr.next = Node(h.val,None,None)

            
            


            
            curr = curr.next
            random_map[h] = curr
            

            

            h = h.next
        


        for i in random_map:

            print(i.val,random_map[i].val)

        h = head
        curr = dummy.next

        while h:
            if h.random in random_map:
                curr.random = random_map[h.random]
            else:
                curr.random  = None

            h= h.next
            curr = curr.next
        
        return dummy.next




