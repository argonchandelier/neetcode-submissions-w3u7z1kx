# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = head
        nx = head.next
        head.next = None
        #print(prev, nx, head.next)

        while nx:
            fnx = nx.next
            nx.next = prev
            prev = nx
            nx = fnx
        
        nx = prev
        #print(nx, nx.val, nx.next.val, nx.next.next.val, nx.next.next.next.val)

        return nx