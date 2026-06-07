class Solution(object):
    def findMinDifference(self, timePoints):
        minu = []
        for t in timePoints:
            h, m = map(int, t.split(':'))
            minu.append(h * 60 + m)
        minu.sort()
        ans = 1440 + minu[0] - minu[-1]
        for i in range(1, len(minu)):
            ans = min(ans, minu[i] - minu[i-1])
        return ans