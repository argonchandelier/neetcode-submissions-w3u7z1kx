# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while True:
            if not slow or not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        '''
        hashmap = {}
        while True:
            if not head:
                return False
            if head in hashmap:
                return True
            hashmap[head] = 1
            head = head.next
        '''