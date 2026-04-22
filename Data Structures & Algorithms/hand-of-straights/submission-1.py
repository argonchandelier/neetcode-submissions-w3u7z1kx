from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        tracker = [0]*groupSize
        summ = 0
        countst = sorted(counts.items())
        mn, mx = min(countst[0]), max(countst[0])

        # if summ isnt 0, i can only move one at a time, until the q is passed;
        # we must also end where the summ is currently 0
        lastn = -1
        for i, (num, count) in enumerate(countst):
            tracker[1:] = tracker[:-1]
            tracker[0] = 0
            summ = sum(tracker)
            #print(f"{lastn = }, {tracker = }, {summ = }, {num = }, {count = }")
            if summ > 0 and lastn+1 < num:
                return False
            tracker[0] = count - summ
            if tracker[0] < 0:
                return False
            lastn = num

        if sum(tracker[:-1]) > 0:
            return False
        return True

