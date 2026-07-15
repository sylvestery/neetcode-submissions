# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Basically 2 pointers
        p1 = list1 
        p2 = list2
        dummy = ListNode()
        curr = dummy

        while p1 or p2:
            while p1 and (not p2 or p1.val <= p2.val):
                curr.next = p1
                p1 = p1.next

                curr = curr.next

            while p2 and (not p1 or p2.val < p1.val):
                curr.next = p2
                p2 = p2.next

                curr = curr.next
        return dummy.next

