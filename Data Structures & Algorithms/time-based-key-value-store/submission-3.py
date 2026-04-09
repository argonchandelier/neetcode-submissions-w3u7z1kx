class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None: # O(1)
        if key in self.hashmap:
            self.hashmap[key][0].append(timestamp)
            self.hashmap[key][1].append(value)
        else:
            self.hashmap[key] = [[timestamp],[value]]

    def get(self, key: str, timestamp: int) -> str: # binary search
        if key not in self.hashmap:
            #print(key, "not in hashmap:", hashmap)
            return ""
        
        timestamps = self.hashmap[key][0]

        if timestamp > timestamps[-1]:
            return self.hashmap[key][1][-1]
        if timestamp < timestamps[0]:
            return ""
        
        n = len(timestamps)
        p1 = 0
        p2 = n-1

        while True:
            pMid = (p1+p2+1) // 2

            num1 = timestamps[p1]
            num2 = timestamps[p2]
            numMid = timestamps[pMid]

            if p1 == p2:
                if num1 == timestamp:
                    return self.hashmap[key][1][p1]
                return self.hashmap[key][1][p1]                 

            if timestamp > numMid:
                p1 = pMid
            elif timestamp < numMid:
                p2 = pMid - 1
            else:
                return self.hashmap[key][1][pMid]


