class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculateTime(piles, k):
            total = 0
            for pile in piles:
                total += math.ceil(float(pile) / k)
            return total
        l, r = 1, max(piles)
        res = r

        while l < r:
            k = l + (r-l) // 2
            totalTime = calculateTime(piles, k)

            if totalTime <= h:
                r = k
            else:
                l = k + 1
        return r