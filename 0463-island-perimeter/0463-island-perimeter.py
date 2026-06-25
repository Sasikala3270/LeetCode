class Solution(object):
    def islandPerimeter(self, grid):
        peri = 0
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    peri += 4
                    
                    if r > 0 and grid[r-1][c] == 1:
                        peri -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        peri -= 2
        return peri