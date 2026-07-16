class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:


        carry = True
        i = 0
        digits.reverse()
        for i in range(len(digits)):
            if not carry:
                break
            elif digits[i] == 9:
                digits[i] = 0
                carry = True
            else:
                digits[i] += 1
                carry = False
        if carry:
            digits.append(1)

        digits.reverse()
        return digits

            
        