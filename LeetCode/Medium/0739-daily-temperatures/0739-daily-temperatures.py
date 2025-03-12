class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_day, _ = stack.pop()
                answer[prev_day] = idx - prev_day
            stack.append((idx, temp))
        return answer