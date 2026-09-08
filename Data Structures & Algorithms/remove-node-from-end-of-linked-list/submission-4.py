# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Dummy node --> incremenet first node n times
        # create antoehr pointer at dumym node --> increment till the end, that node behind id the node we want to break

        dummy = ListNode(0, head)
        l, r = dummy, dummy
        #invemrenet till nth node
        for _ in range(n):
            r = r.next
        
        #now incremenet the right pointer till tail
        while r.next:
            l = l.next
            r = r.next
        
        #reassign pointers
        tmp = l.next.next
        l.next = tmp
        return dummy.next
        
