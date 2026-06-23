class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l  
        up = [0] * (m + 1)
        down = [0] * (m + 1)

        
        for i in range(m + 1):
            up[i] = i          
            down[i] = m - i   

        for _ in range(2, n):
            new_up = [0] * (m + 1)
            new_down = [0] * (m + 1)

            pref = 0
            for i in range(m + 1):
                new_up[i] = pref
                pref = (pref + down[i]) % MOD

            suff = 0
            for i in range(m, -1, -1):
                new_down[i] = suff
                suff = (suff + up[i]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD