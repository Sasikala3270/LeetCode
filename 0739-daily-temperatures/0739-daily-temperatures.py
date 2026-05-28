class Solution(object):
    def dailyTemperatures(self, temp):
        n = len(temp)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temp[i] > temp[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        return ans
        