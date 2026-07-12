class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        n = len(temperatures)
        result = [0] * n
        stk = []
        for i, temp in enumerate(temperatures):
            while stk and temp > stk[-1][0]:
                result[stk[-1][1]] = i -stk[-1][1] 
                stk.pop()
            stk.append((temp, i))
        return result



        # 30 38 30 36 35 40
        # 1. ? 1 2 1
        # 30 
        #   (40, 5) (28, 6) -> 
# 1 4 1 2 1 0 0