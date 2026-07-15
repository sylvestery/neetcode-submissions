class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        def find_rot() -> int:
            left = 0
            right = n-1
            while left < right:
                mid = left + (right -left) //2
                if nums[right] < nums[mid]:
                    left = mid+1
                else:
                    right = mid
            return left
        pivot = find_rot()
        left = 0
        right = n-1
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot -1
            
        while left<= right:
            mid = left + (right -left) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        print(left, right)
        return -1
        

           
        