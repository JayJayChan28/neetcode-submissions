# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #two poitner approach 
        new_LL = ListNode(0, None) # create dummy for new LL
        dummy = new_LL
        remainder = 0 #count remainder 
        while l1 or l2 or remainder:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            node_val = (l2_val + l1_val + remainder) % 10
            remainder = (l2_val + l1_val + remainder) // 10
            print(remainder)
            print(l1_val + l2_val)
            new_LL.next = ListNode(node_val, None)
            new_LL = new_LL.next
            l1 = l1.next if l1 else None #point to next value in LL if its none then we walt to contineu
            l2 = l2.next if l2 else None
        return dummy.next











        