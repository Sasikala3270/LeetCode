class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m

        size = 2 * m

        def mat_mul(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if A[i][k]:
                        aik = A[i][k]
                        for j in range(size):
                            if B[k][j]:
                                C[i][j] = (C[i][j] + aik * B[k][j]) % MOD
            return C

        def mat_pow(M, p):
            R = [[0] * size for _ in range(size)]
            for i in range(size):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                p >>= 1

            return R

        T = [[0] * size for _ in range(size)]

     
        for i in range(m):
            for j in range(i + 1, m):
                T[i][m + j] = 1

      
        for i in range(m):
            for j in range(i):
                T[m + i][j] = 1

        P = mat_pow(T, n - 1)

        ans = 0

        
        for start in range(size):
            ans = (ans + sum(P[start])) % MOD

        return ans