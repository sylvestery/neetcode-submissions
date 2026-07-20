class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)
        
        while len(h) > 1: # if two or more
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)
            if x == y:
                continue
            elif x < y:
                heapq.heappush(h, -(y-x))
            else :
                heapq.heappush(h, -(x-y))

        print(h)
        return 0 if not h else -h[0]
        
        