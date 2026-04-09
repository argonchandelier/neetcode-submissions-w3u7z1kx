class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottestF = [0] * n
        hottestB = [0] * n
        warmer_days_before_stack = []
        answer = [0] * n

        for i in range(n):
            temp = temperatures[i]
            while warmer_days_before_stack:
                check_day = warmer_days_before_stack[-1]
                check_temp = temperatures[check_day]
                if check_temp < temp:
                    warmer_days_before_stack.pop()
                    answer[check_day] = i - check_day
                else:
                    break
            warmer_days_before_stack.append(i)
        
        return answer