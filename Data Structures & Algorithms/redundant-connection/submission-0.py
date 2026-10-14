class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        res = []

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootx, rooty = find(x), find(y)

            if rootx == rooty:
                return False
            parent[rooty] = rootx
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u,v]

        return res
        