class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = list(range(n))
        rank = [0] * n

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i,j):
            rooti , rootj = find(i) , find(j)

            if rooti == rootj:
                return False

            if rank[rooti] > rank[rootj]:
                parent[rootj] = rooti
            elif rank[rootj] > rank[rooti]:
                parent[rooti] = rootj
            else:
                parent[rootj] = i
                rank[rooti] += 1
            return True

        edges = [] 

        for i in range(n):
            xi , yi = points[i]
            for j in range(i + 1, n):
                xj , yj = points[j]

                cost = abs(xi - xj) + abs(yi -yj)

                edges.append((cost, i, j))
            
        edges.sort()
        
        total_cost = 0
        edges_connected = 0

        for cost, u, v in edges:
            if union(u,v):
                total_cost += cost
                edges_connected += 1
                if edges_connected == n - 1:
                    break
        
        E = total_cost
        return E


    





    
    




        