# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer technique
        dummy_node = ListNode(0, head) # dummy node 
        l, r = dummy_node, dummy_node
        while n != 0:
            r = r.next
            n -= 1
        print(l.val)
        print(r.val)
        
        while r.next: #while there is still a next pointer for r, meaning that we are not at the end of the LL
            r = r.next
            l = l.next
  
        
        #reorder pointers
        l.next = l.next.next

        return dummy_node.next


            