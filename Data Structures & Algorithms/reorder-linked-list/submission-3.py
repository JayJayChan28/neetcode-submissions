# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle --> split LL's
        dummy = head
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next # set pointer to second LL
        slow.next = None # break the LL to split LL

        #now we reverse l2
        prev = None
        curr = l2
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        self.merge_LL(dummy, prev)
        
        #now we merge the two LL
    def merge_LL(self, l1, l2):
        while l2:
            tmp = l1.next
            l1.next = l2
            l1 = tmp
            tmp_l2 = l2.next
            l2.next = l1
            l2 = tmp_l2
        





            

            



