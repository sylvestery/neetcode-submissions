class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        # minimum number of cycles.
        # We can count how many dupes we have?
        # do the most complex and do unoques inbetween.
        # mark how many cycles we wait before op again?
        # x -> [2] 1 2 1+1 5
        # y -> [2] x[1]
        # 1 < 2 idle [x[0]] y[1]
        # x, y, x, idle, x, y
        # 
        # AAA B C
        # A: 3 [0] 2   1
        # B: 1 [0] 0 2
        # C: 1 [0] 0 3
        # A  A: 3 1 
        # C  A: 2  2
        # B A: 1  3
        # ? 4 
        # A 5 3 + (1 + n)
        # A 5 + (1 + n) = 9
        taskFreq = Counter(tasks)
        nextTask = []
        for task, freq in taskFreq.items():
            heapq.heappush(nextTask, (-freq, task))
        print(taskFreq)
        cycles = 0
        waitQueue = deque()
        
        while nextTask or waitQueue:
            cycles += 1
                

            if nextTask:
                freq, next = heapq.heappop(nextTask)
                newFreq = freq+1
                # store them in FIFO
                if newFreq != 0:
                    waitQueue.append((newFreq, next, cycles+n))
            if waitQueue and waitQueue[0][2] == cycles:
                (freq, name, cycles) = waitQueue.popleft()
                heapq.heappush(nextTask, (freq, name))

        return cycles

        
        