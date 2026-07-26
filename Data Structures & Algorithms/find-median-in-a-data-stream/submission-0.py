class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []
        

    def addNum(self, num: int) -> None:
        if self.larger and num > self.larger[0]:
            heapq.heappush(self.larger, num)
        else:
            heapq.heappush(self.smaller, -num)
        while len(self.larger)  - len(self.smaller) > 1:
            nx = heapq.heappop(self.larger)
            heapq.heappush(self.smaller, -nx)
        while len(self.smaller)  - len(self.larger) > 1:
            nx = heapq.heappop(self.smaller)
            heapq.heappush(self.larger, -nx)




        

    def findMedian(self) -> float:
        n = len(self.smaller)
        m = len(self.larger)
        if n == m:
            return (-self.smaller[0] + self.larger[0])/2
        elif n > m: 
            return -self.smaller[0]
        else:
            return self.larger[0]


        
        