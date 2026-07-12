# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def reverse(node):
            prev = None
            temp = None
        
            while node:
            
                temp = node.next
                node.next = prev
                prev = node

                node = temp
            

            return prev

        n = 0
        curr = head
        while curr:
            n+=1
            curr= curr.next

        curr = head
        c = 1
        while (n+1)//2 !=c:
            # print(curr.val)
            curr = curr.next
            c+=1
        
        # print('++++++++++++++++++++++++++++++++++++++', n)
        new_list  = curr.next
        

        l2  = reverse(new_list)
        l1 = head
        curr.next = None
        
        dummy = ListNode()
        dummy_next = l1
        # print(l1.val,l2.val)


        # while l1:
        #  print(l1.val)
        #  l1 = l1.next
        # print('+++++++++++++++++++++++++++++++')
        # while l2:
        #     print(l2.val)
        #     l2 = l2.next
        

        while l1 and l2:
            print(l1.val,l2.val)
            
            temp1= l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1

            # print(l1.val,l2.val,temp1.val,temp2.val)

            l1 = temp1
            l2 = temp2
        
        head = dummy
            


            



            

        


    

            
