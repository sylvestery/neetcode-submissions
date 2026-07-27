class Solution:
    def countBits(self, n: int) -> List[int]:
       # 1000 is only 10 bits
        # basically O(1) operation 
        result = []
        for num in range(n+1):
            curr = num
            total = 0
            while curr:
                total+= curr & 1
                curr >>=1
            result.append(total)
        return result
