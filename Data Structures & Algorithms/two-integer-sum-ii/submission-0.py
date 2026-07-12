class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        n =len(numbers)
        left = 0
        right = n-1
        while left < right :
            curSum = numbers[left] + numbers[right]
            diff = target-curSum
            if diff == 0:
                return [left + 1, right + 1]
            elif diff > 0: # if target is bigger than sum
                left += 1
            else: # if target is less than sum
                right -= 1
        return []
        
        