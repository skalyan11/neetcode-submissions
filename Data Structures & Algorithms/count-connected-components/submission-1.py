class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m = {i: [] for i in range(n)}
        for n1, n2 in edges:
            m[n1].append(n2)
            m[n2].append(n1)
        
        visit = set()
        def dfs(node):
            visit.add(node)
            for nei in m[node]:
                if nei not in visit:
                    dfs(nei)
            
    
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        
        return count