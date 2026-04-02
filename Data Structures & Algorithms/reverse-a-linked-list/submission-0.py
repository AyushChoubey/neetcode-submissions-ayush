# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        next_ = None
        while(current != None):
            if current.next == None:
                head = current 
                head.next = prev
                break
            next_ = current.next
            current.next = prev
            prev = current 

            current = next_

        return head 

            
            
            
            

        