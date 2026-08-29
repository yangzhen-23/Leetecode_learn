"""
15. 三数之和
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = []
        i = 0
        for i in range(n -2):
            if nums[i] > 0: break
            if i > 0 and nums[i - 1] == nums[i]: continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                    while l < r and nums[l - 1] == nums[l]: l += 1
                elif s > 0:
                    r -= 1
                    while l < r and nums[r + 1] == nums[r]: r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]: l += 1
                    while l < r and nums[r + 1] == nums[r]: r -= 1
        return result