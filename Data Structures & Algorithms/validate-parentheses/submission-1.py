class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        pairs = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        stk = []
        for c in s:
            if c in pairs:
                if stk and pairs[c] == stk[-1]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return len(stk) == 0

        