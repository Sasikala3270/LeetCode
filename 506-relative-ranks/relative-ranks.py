class Solution(object):
    def findRelativeRanks(self, score):
        n = len(score)
        arr = sorted([(score[i], i) for i in range(n)], reverse = True)

        ans = [""] * n
        for rank, (val, idx) in enumerate(arr):
            if rank == 0:
                ans[idx] = "Gold Medal"
            elif rank == 1:
                ans[idx]= "Silver Medal"
            elif rank == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx]= str(rank + 1)
        return ans