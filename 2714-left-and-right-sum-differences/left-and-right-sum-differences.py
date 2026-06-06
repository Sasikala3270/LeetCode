class Solution(object):
    def leftRightDifference(self, nums):
        tot = sum(nums)
        left_sum = 0
        ans = []

        for num in nums:
            tot -= num

            ans.append(abs(left_sum - tot))
            left_sum += num
        return ans
        