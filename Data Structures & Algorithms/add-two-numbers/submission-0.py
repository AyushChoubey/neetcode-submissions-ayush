# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        str1 = ''
        str2 = ''

        while l1:

            str1+= str(l1.val)
            l1 = l1.next

        while l2:
            str2 += str(l2.val)
            l2 = l2.next
        
        

        s = str(int(str1[::-1])+int(str2[::-1]))
        print(s)
        s = s[::-1]
        dummy = ListNode(0,None)
        curr= dummy
        print(s)

        while s != '':
            curr.next = ListNode(int(s[0]), None)
            
            curr = curr.next

            
            s = s[1:]

        return dummy.next
        