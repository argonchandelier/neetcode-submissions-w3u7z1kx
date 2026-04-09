#"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
#"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldH = {}
        h = {}
        conversion = {}
        n = 0
        last = None
        check = head
        newHead = None
        while check:
            newNode = Node(check.val)
            if n == 0:
                newHead = newNode
            h[n] = newNode
            oldH[check] = n
            if last:
                last.next = newNode
            last = newNode

            n += 1
            check = check.next

        check2 = head
        i = 0
        while check2:
            r = check2.random
            ri = None
            if r in oldH:
                ri = oldH[r]
            conversion[i] = ri

            check2 = check2.next
            i += 1

        print(conversion)
        check3 = newHead
        i = 0
        while check3:
            ci = conversion[i]
            if ci != None:
                check3.random = h[ci]

            i += 1
            check3 = check3.next
        
        return newHead



        

        
