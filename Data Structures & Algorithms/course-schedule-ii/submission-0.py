class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i: [] for i in range(numCourses)}
        visited, cycle = set(), set()
        res = []

        for crs, pre in prerequisites:
            premap[crs].append(pre)


        #### 0 - 1
        #### 1 - 2
        ##### 2 - 0

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for pre in range(numCourses):
            if not dfs(pre):
                return []
        return res
            








        
