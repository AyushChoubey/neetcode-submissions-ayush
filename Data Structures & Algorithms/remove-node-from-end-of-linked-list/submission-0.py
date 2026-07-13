# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        l = 0
        curr = head
        while curr:
            curr = curr.next
            l+=1

        print(l)

        t = l-n
        curr = head 
        print(t,l,n)

        if t== 0:
        
            head = head.next
            



        else:   
            while t >1:
                curr= curr.next
                t-=1
            if curr.next:
                temp = curr.next.next
            else:
                temp  = None

            curr.next = temp 

        return head





        