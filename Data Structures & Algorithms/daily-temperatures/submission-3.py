class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, elm in enumerate(temperatures):
            while stack and stack[-1][0] < elm:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append([elm, i])
        return res