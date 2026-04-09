# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            if not list2:
                return None
            return list2
        if not list2:
            return list1
        
        val1 = list1.val
        val2 = list2.val

        if val1 < val2:
            first = list1
            list3 = list1
            list1 = list1.next
        else:
            first = list2
            list3 = list2
            #print(list2.val)
            list2 = list2.next
            #print(list2.val)

        while True:
            if not list1:
                list3.next = list2
                break
            if not list2:
                list3.next = list1
                break

            val1 = list1.val
            val2 = list2.val
            #'''
            if val1 < val2:
                #nxt = list1
                #print("A")
                list3.next = list1
                list1 = list1.next
                #print("B")
            else:
                #print("C")
                #q=list2
                #print(list2, list3, list3.next)
                list3.next = list2
                list2 = list2.next
                #print("D")
            
            list3 = list3.next
                #'''
            #'''
            
                #'''
            #break
            
        return first

