class Solution:
    def processStr(self, s: str, k: int) -> str:
        len = 0
        for c in s:
            if c == '*':
                len = max(0, len - 1)
            elif c == '#':
                len *= 2
            elif c == '%':
                pass
            else:
                len += 1
        if k >= len:
            return '.'
        for c in reversed(s):
            if c == '*':
                len += 1
            elif c == '#':
                len //= 2
                if k >= len:
                    k -= len
            elif c == '%':
                k = len - 1 -k
            else:
                len -= 1
                if k == len:
                    return c