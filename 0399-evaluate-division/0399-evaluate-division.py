class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the adjacency graph
        g = collections.defaultdict(dict)
        for (u, v), val in zip(equations, values):
            g[u][v] = val
            g[v][u] = 1.0 / val
            
        # Step 2: Compact DFS function to find the running product path
        def dfs(start: str, target: str, visited: set) -> float:
            if start == target: 
                return 1.0
            visited.add(start)
            for neighbor, weight in g[start].items():
                if neighbor not in visited:
                    product = dfs(neighbor, target, visited)
                    if product != -1.0:
                        return weight * product
            return -1.0

        # Step 3: Fast lookup list comprehension
        return [dfs(c, d, set()) if c in g and d in g else -1.0 for c, d in queries]
