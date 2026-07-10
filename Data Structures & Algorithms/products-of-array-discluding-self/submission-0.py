class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        prefix_mult = [1]
        suffix_mult = [1]
        for i, num in enumerate(nums):
            print(i, num)
            prefix_mult.append(prefix_mult[i] * num)
        
        print(prefix_mult)
        for i in range(n-1, -1, -1):
            num = nums[i]
            print(i, num)
            suffix_mult.append(suffix_mult[n-i-1] * num)
        print(list(reversed(suffix_mult)))
        suffix_mult = list(reversed(suffix_mult))
        output =[]
        for i in range(n):
            output.append(prefix_mult[i] * suffix_mult[i+1])
        return output