from collections import defaultdict
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        dres = nums
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                cnt[nums[j]] += 1
                length = j - i + 1
                if cnt[target] > length // 2:
                    ans += 1
        return ans