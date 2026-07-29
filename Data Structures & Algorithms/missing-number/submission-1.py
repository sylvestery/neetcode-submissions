class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = set(nums)
        expected = 0

        for i in range(1, len(nums)+1):
            expected ^= i
        print(expected)
        calculated = 0
        for num in nums:
            calculated ^= num

        return calculated ^ expected
       # Bit representation of the number
       #  