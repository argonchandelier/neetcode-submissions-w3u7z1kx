# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        
        # middle point, rounding up (higher of 2 medians if even size), connects to none
        # loop once to find size n, calc median
        # loop again until median, while setting next to be previous
        # set median next to point to None, then loop back and forth at the same time
        # odd n: forward++, set next to med (current backward), backward++, set next to forward, forward++, set next to backward, stop when forward is None immediately
        # even ex: 0,1,2,3
        # even n: backward++, set next to med (current forward), etc., stop when forward is None again

        check = head
        n = 0
        while check: # could also do a fast to indicate middle, then even or odd depends on whether .next or .next.next DNE first, and slow reverses links
            n += 1
            check = check.next
        mid = n // 2
        
        print("n:", n)
        forward = head
        prevPrev = None
        for i in range(mid):
            prev = forward
            forward = forward.next
            prev.next = prevPrev
            prevPrev = prev
        backward = ListNode(forward.val, prev)
        print("med:", forward.val)
        print(forward.val, backward.val, forward.next.val, backward.next.val)

        prevBNext = None
        prevFNext = None
        if n % 2 == 0: # even n, start back, then forth, else start forth first which is what loop does already
            prevB = backward
            backward = backward.next
            prevBNext = forward
        while forward:
            # step forth, then back, then loop
            prevF = forward
            forward = forward.next
            prevF.next = prevFNext
            prevFNext = backward

            prevB = backward
            backward = backward.next
            prevB.next = prevBNext
            prevBNext = forward
        
        return# backward








'''
        evens = head
        odds = head.next
        prevEvens = evens
        prevOdds = odds
        prevPrevOdds = None


        # 0,1,2,3,4 -> 0,4,1,3,2 # odd len ends in even
        # 0,1,2,3 -> 0,3,1,2 # even len ends in odd 
        while True:
            if not evens:
                prevEvens.next = odds
                odds.next = prevOdds
                break
            if not odds:
                evens.next = prevOdds
                break
            if evens and evens.next:
                prevEvens = evens
                evens = evens.next.next
                prevEvens.next = evens
            if odds and odds.next:
                odds = odds.next.next
                prevOdds.next = prevPrevOdds
                prevPrevOdds = prevOdds
                prevOdds = odds
        
        print(head.val, head.next.val, head.next.next.val) #, head.next.next.next.val)
        #print(head.next.next.next.next.val)
        return head
        '''
                

