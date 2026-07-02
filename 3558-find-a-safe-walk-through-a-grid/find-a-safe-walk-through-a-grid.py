import heapq
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        dist = [[-1] * n for _ in range(m)]

        start = health - grid[0][0]
        if start <= 0:
            return False

        pq = [(-start, 0, 0)]
        dist[0][0] = start

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            h, x, y = heapq.heappop(pq)
            h = -h

            if x == m - 1 and y == n - 1:
                return True

            if h < dist[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    nh = h - grid[nx][ny]
                    if nh > 0 and nh > dist[nx][ny]:
                        dist[nx][ny] = nh
                        heapq.heappush(pq, (-nh, nx, ny))

        return False