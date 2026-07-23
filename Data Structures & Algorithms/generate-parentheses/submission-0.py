class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result =[]

        def backtrack(curr, op, close):
            if close > op:
                return
            if len(curr) == n * 2 and op == close:
                result.append(''.join(curr[:]))
                return
            if op < n:
                curr.append("(")
                backtrack(curr, op+1, close)
                curr.pop()
            if close < op:
                curr.append(")")
                backtrack(curr, op, close+1)
                curr.pop()
        backtrack([], 0, 0)
        return result
        