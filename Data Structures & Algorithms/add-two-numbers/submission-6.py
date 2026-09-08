# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #321
        #654

        p1, p2 = l1, l2
        new_node = ListNode(0)
        dummy_node = new_node
        
        remainder = 0 
        while p1 or p2 or remainder:
            val_1 = p1.val if p1 else 0
            val_2 = p2.val if p2 else 0
            total = val_1 + val_2 + remainder
            remainder = total // 10
            val = total % 10
            dummy_node.next = ListNode(val)
 
            dummy_node = dummy_node.next

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        return new_node.next

            
