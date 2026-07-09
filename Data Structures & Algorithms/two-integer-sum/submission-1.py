class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i, num in enumerate(nums):
            mapping[num] = i
        print(mapping)
        for i, num in enumerate(nums):
            diff = target-num
            if diff in mapping and mapping[diff] != i:
                return [i, mapping[target-num]]
        return []
                

        