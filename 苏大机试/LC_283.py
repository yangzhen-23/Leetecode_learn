"""
283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        number = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                number += 1
            elif number > 0:
                nums[i - number] = nums[i]
                nums[i] = 0