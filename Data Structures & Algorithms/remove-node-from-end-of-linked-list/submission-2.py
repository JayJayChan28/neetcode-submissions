# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #create dummy node
        dummy = ListNode(0, head)
        l, r = dummy, dummy
        # move r pointer n times
        while n != 0:
            r = r.next
            n -= 1
        print(r.val)
        print(l.val)
        # r-l = nth node --> do l.next for nth node
        while r.next:
            r = r.next
            l = l.next
        print(r.val)
        print(l.val)
        prev_node = l
        nth_node = l.next
        prev_node.next = nth_node.next
        return dummy.next


