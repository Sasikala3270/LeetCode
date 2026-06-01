class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse = True)
        tot = 0
        for i in range(len(cost)):
            if (i+1) % 3 != 0:
                tot += cost[i]
        return tot
        