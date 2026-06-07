class Solution(object):
    def findUnsortedSubarray(self, nums):
        sorted_num = sorted(nums)
        left = 0
        while left < len(nums) and nums[left] == sorted_num[left]:
            left += 1
        right = len(nums) - 1
        while right >= 0 and nums[right] == sorted_num[right]:
            right -= 1
        return right - left + 1 if right > left else 0