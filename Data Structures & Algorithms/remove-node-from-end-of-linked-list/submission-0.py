# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = 0
        check = head
        while check:
            s += 1
            check = check.next
        ri = s-n
        if ri == 0:
            return head.next
        ll = head
        prevll = None
        for i in range(ri):
            prevll = ll
            ll = ll.next
        prevll.next = ll.next

        return head