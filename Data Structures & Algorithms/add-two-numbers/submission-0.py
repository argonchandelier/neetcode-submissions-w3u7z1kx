# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        over = 0
        l3 = None
        last = None
        while l1 or l2:
            n1=0
            n2=0
            if l1:
                n1 = l1.val
            if l2:
                n2 = l2.val
            dSum = n1 + n2 + over
            over = dSum // 10
            dSum = dSum % 10

            newNode = ListNode(dSum)
            if last:
                last.next = newNode
            else:
                head = newNode
            last = newNode

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if over > 0:
            newNode = ListNode(over)
            last.next = newNode
        
        return head



        