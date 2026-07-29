class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = set(nums)
        for i in range(len(nums)+1):
            if i not in expected:
                return i
        return -1
       # Bit representation of the number
       #  