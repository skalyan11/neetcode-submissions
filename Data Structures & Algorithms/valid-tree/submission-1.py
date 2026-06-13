class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = {i : [] for i in range(n)}
        
        for n1, n2 in edges:
            m[n1].append(n2)
            m[n2].append(n1)
        
        visit = set()

        def dfs(node, parent):
            visit.add(node)
            for nei in m[node]:
                if nei not in visit:
                    if dfs(nei, node):
                        return True
                elif nei != parent:
                    return True
            return False
        
        if dfs(0, - 1):
            return False
        
        return len(visit) == n