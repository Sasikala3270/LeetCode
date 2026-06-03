class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def calc(st1, du1, st2, du2):
            min_end = min(s+d for s, d in zip(st1, du1))

            ans = float('inf')
            for s, d in zip(st2, du2):
                ans = min(ans, max(min_end, s) + d)
            return ans

        land_first = calc(landStartTime, landDuration, waterStartTime, waterDuration)
        water_first = calc(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(land_first, water_first)
        