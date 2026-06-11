class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q = deque([1])
        visited = {1}
        depth = -1
        while q:
            depth += 1
            for _ in range(len(q)):
                u = q.popleft()
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
        return pow(2, depth - 1, MOD)