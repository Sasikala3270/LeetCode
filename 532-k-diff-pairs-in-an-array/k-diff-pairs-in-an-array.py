class Solution(object):
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        if k == 0:
            count = {}
            ans = 0
            for num in nums:
                count[num] = count.get(num, 0) + 1

            for val in count.values():
                if val > 1:
                    ans += 1
            return ans
        s = set(nums)
        ans = 0
        for num in s:
            if num + k in s:
                ans +=1
        return ans