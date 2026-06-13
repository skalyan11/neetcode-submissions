class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            m[crs].append(pre)

        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if m[crs] == []:
                return True
            
            visiting.add(crs)
            for pre in m[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            m[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True