class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0
        # Find the minimum time 
        # Likely a search over a space
        # Amount of time to finish banana
        # pile / speed = time
        # 
        left = 1
        right = max(piles) # Upper bound is the number if bananas
        def canFinish(speed):
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / speed)
            return totalTime <= h
        while left < right:
            mid = left + (right - left) //2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        print(left, right)
        return left

        
        