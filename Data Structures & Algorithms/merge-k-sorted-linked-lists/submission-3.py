# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = None

        for linked_list in lists:
            merged = self.merge_lists(merged, linked_list)
        return merged


    def merge_lists(self, l1, l2):
        new_linked = ListNode()
        curr = new_linked
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            elif l1.val >= l2.val:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
        while l1:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
        while l2:
            curr.next = l2
            curr = curr.next
            l2 = l2.next
        return new_linked.next




                

