class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        h = []
        for num, frequency in count.items():
            heapq.heappush(h, (frequency, num))
            if len(h) > k:
                heapq.heappop(h)
        print(h)
        return [x[1] for x in h]
