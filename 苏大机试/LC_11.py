"""
11. 盛最多水的容器
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0

        while l < r:
            min_height = min(height[l], height[r])
            width = r - l
            water = min_height * width
            max_water = max(water, max_water)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water