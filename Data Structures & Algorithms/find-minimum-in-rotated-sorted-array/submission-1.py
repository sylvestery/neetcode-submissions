# 3 4 5 6 1 2
# 1 2 3 4 5 6
# Find the first time the number decreases? requires O(n)
# L and R need to somehow swap, or to skip a side
# if if l > mid -> l needs to move left 
# 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        left = 0
        right = n
        while left <right:
            mid = left + (right - left) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid

        return nums[left if left < n else 0]