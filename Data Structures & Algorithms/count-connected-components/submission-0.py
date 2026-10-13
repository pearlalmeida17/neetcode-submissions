class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashmap = {i : [] for i in range(n)}

        for e1, e2 in edges:
            hashmap[e1].append(e2)
            hashmap[e2].append(e1)
        
        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)

            for neighbor in hashmap[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components
            
