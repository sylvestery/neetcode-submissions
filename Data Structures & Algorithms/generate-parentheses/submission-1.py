class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result =[]

        def backtrack(curr, op, close):
            if close > op or op > n:
                return
            if op == close == n:
                result.append(''.join(curr[:]))
                return
            curr.append("(")
            backtrack(curr, op+1, close)
            curr.pop()
            curr.append(")")
            backtrack(curr, op, close+1)
            curr.pop()
        backtrack([], 0, 0)
        return result
        