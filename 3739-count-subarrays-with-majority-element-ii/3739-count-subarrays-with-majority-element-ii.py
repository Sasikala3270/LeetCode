from bisect import bisect_left, insort
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        prefix = 0
        ans = 0
        seen = [0]
        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1
            ans += bisect_left(seen, prefix)
            insort(seen, prefix)
        return ans