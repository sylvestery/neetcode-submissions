class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Top sort
        indegree = defaultdict(int) 
        graph = defaultdict(list)
        for  pre,crs in prerequisites:
            indegree[crs] += 1
            graph[pre].append(crs)
        q = deque([node for node in range(numCourses) if indegree[node] == 0])
        print(q)
        
        while q:
            node = q.popleft()
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        return all([indegree[node] == 0 for node in range(numCourses)])
    
