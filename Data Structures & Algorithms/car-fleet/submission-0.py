class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        times = [0] * n
        for i in range(n):
            #times[i] = -(-(target - position[i]) // speed[i])
            times[i] = [((target - position[i]) / speed[i]), i]
        
        sorted_times = sorted(times, key=lambda x:x[0])[::-1]
        
        # a,b: if b has slower time but higher pos, a is part of a fleet, kick out a
        # a,b: same time, in same fleet, kick out a
        #latest_time = sorted_times[0]
        latest_t = sorted_times[0][0]
        latest_i = sorted_times[0][1]
        nFleets = 1
        for i in range(1, n):
            check = sorted_times[i]
            check_t = check[0]
            check_i = check[1]
            if check_t == latest_t: # meet up at end, counts as same fleet
                if position[check_i] > position[latest_i]: # use higher position
                    latest_i = check_i
            elif position[latest_i] > position[check_i]: # meet up in middle, same fleet
                continue
            else:
                nFleets += 1
                latest_t = check_t
                latest_i = check_i


        
        print(times, "---", sorted_times)

        return nFleets