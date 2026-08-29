"""
题10：募集捐款
有n个居民，第i个居民想捐的款为donates[i],志愿者会上门募集捐款，有一条规定，志愿者不能连续在两间相邻的房屋内收集捐款，
请计算志愿者能够募集到捐款的最高金额。
原题：leetcode198.打家劫舍https://leetcode.cn/problems/house-robber/description/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if n >= 2:
            dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i -2] + nums[i])
        return max(dp)