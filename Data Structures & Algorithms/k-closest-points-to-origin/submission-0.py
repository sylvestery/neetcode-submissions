class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []
        def distance(p1, p2):
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            return math.sqrt(dx ** 2 + dy ** 2)
        
        h = []
        origin = [0, 0]
        for point in points:
            print(point)
            dist_origin = distance(point, origin)
            heapq.heappush(h, (-dist_origin, point))
            while len(h) > k:
                heapq.heappop(h)



        return [point for dist, point in h]

        
