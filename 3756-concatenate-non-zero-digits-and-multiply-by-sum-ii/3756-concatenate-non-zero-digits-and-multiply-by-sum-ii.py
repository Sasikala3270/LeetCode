from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        solendivar = (s, queries)

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        m = len(digits)

        if m == 0:
            return [0] * len(queries)

        pre_sum = [0] * (m + 1)
        for i in range(m):
            pre_sum[i + 1] = pre_sum[i] + digits[i]

        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        pre_num = [0] * (m + 1)
        for i in range(m):
            pre_num[i + 1] = (pre_num[i] * 10 + digits[i]) % MOD

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r)

            if left == right:
                ans.append(0)
                continue

            length = right - left
            num = (pre_num[right] - pre_num[left] * pow10[length]) % MOD
            digit_sum = pre_sum[right] - pre_sum[left]
            ans.append((num * digit_sum) % MOD)

        return ans