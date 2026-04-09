# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        while True:
            if not head:
                return False
            if head in hashmap:
                return True
            hashmap[head] = 1
            head = head.next