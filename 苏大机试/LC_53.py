"""
53. 最大子数组和
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。
"""
# 暴力
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        for i in range(n):
            for j in range(i, n):
                sub_sum = sum(nums[i:j+1])
                max_sum = max(sub_sum, max_sum)
        return max_sum

# 暴力upgrade
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        for i in range(n):
            sub_sum = 0
            for j in range(i,n):
                sub_sum += nums[j]
                max_sum = max(max_sum, sub_sum)
        return max_sum

# 优化算法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n 
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            max_sum = max(max_sum, dp[i])
        return max_sum