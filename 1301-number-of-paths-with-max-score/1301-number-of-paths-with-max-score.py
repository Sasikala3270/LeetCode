from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        # dpScore[i][j] = maximum score from (i,j) to end
        # dpWays[i][j] = number of ways to achieve that maximum score
        dpScore = [[-1] * n for _ in range(n)]
        dpWays = [[0] * n for _ in range(n)]

        dpScore[n - 1][n - 1] = 0
        dpWays[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X':
                    continue
                if i == n - 1 and j == n - 1:
                    continue

                bestScore = -1
                ways = 0

                # Move down
                if i + 1 < n and dpScore[i + 1][j] != -1:
                    if dpScore[i + 1][j] > bestScore:
                        bestScore = dpScore[i + 1][j]
                        ways = dpWays[i + 1][j]
                    elif dpScore[i + 1][j] == bestScore:
                        ways = (ways + dpWays[i + 1][j]) % MOD

                # Move right
                if j + 1 < n and dpScore[i][j + 1] != -1:
                    if dpScore[i][j + 1] > bestScore:
                        bestScore = dpScore[i][j + 1]
                        ways = dpWays[i][j + 1]
                    elif dpScore[i][j + 1] == bestScore:
                        ways = (ways + dpWays[i][j + 1]) % MOD

                # Move diagonal
                if i + 1 < n and j + 1 < n and dpScore[i + 1][j + 1] != -1:
                    if dpScore[i + 1][j + 1] > bestScore:
                        bestScore = dpScore[i + 1][j + 1]
                        ways = dpWays[i + 1][j + 1]
                    elif dpScore[i + 1][j + 1] == bestScore:
                        ways = (ways + dpWays[i + 1][j + 1]) % MOD

                if bestScore == -1:
                    continue

                value = 0
                if board[i][j] not in ('S', 'E'):
                    value = int(board[i][j])

                dpScore[i][j] = bestScore + value
                dpWays[i][j] = ways % MOD

        if dpScore[0][0] == -1:
            return [0, 0]

        return [dpScore[0][0], dpWays[0][0]]