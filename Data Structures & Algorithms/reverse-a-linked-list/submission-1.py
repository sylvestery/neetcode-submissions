# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, None)
        # For a given node need to swap next from the next node to the previous.
        # 0 1 2 3
        # 0 -> 1 -> 2 -> 3
        # 0 <- 1 <- 2 <- 3
        # Is this in place?
        dummy = head
        curr = dummy
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev 
            prev = curr
            curr = tmp
        return prev
            
        