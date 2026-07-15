from sortedcontainers import SortedList
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        times = self.store[key]
        if timestamp < times[0][1]:
            return ""
        # Execute binary search to find the value closest to timestamp but not.
        left = 0 
        right = len(times) -1
        while left <= right:
            mid = left + (right - left) // 2
            if times[mid][1] == timestamp:
                return times[mid][0]
            if times[mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid -1
        return times[right][0] 

        
