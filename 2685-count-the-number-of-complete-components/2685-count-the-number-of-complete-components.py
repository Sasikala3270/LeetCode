from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            stack = [node]
            vertices = 0
            degree_sum = 0

            while stack:
                cur = stack.pop()
                if visited[cur]:
                    continue
                visited[cur] = True
                vertices += 1
                degree_sum += len(graph[cur])

                for nei in graph[cur]:
                    if not visited[nei]:
                        stack.append(nei)

            return vertices, degree_sum

        for i in range(n):
            if not visited[i]:
                vertices, degree_sum = dfs(i)

                # Number of edges in the component
                edges_count = degree_sum // 2

                # Complete graph has v*(v-1)/2 edges
                if edges_count == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans
        