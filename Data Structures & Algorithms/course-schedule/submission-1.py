class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        print(preMap)
        seen = set()
        def dfs(crs):
            if crs in seen:
                return False
            if preMap[crs] == []:
                return True
            seen.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            seen.discard(crs)
            preMap[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
        

        