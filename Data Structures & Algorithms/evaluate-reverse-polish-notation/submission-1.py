class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0 
        stk = []
        operands = set('+-/*')
        print(operands)
            
        for token in tokens:
            print(stk)
            if token in operands:
                if len(stk) >= 2:
                    right = stk.pop()
                    left = stk.pop()
                    nxt = 0
                    match token:
                        case '+':
                            nxt = left + right
                        case '-':
                            nxt = left - right
                        case '*':
                            nxt = left * right
                        case '/':
                           nxt = int(float(left) / right)
                    stk.append(nxt)
            else:
                stk.append(int(token))
        print(stk)    
        return stk[-1] if stk else 0
























    # [1, 2]
    # + 
    # [3]
    #[3, 3]
    # *
    # 9
    # 9, 4
    # -
    # 5
    #[1, 2, 2, 4]
    # +
    # *
    #6
    # *