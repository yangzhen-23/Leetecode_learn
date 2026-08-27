"""
给一串字符串，提取其中的连续数字，对于连续数字组成的正整数，给定一个区间，返回符合该区间的正整数的最大值，最小值。
"""
class Solution:
    def FindMinMaxNumber(self, s: str, left: int, right: int) -> tuple:
        nums = []
        n = len(s)
        i = 0

        while i < n:
            if s[i].isdigit():
                j = i
                while j < n and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                if left <= num <= right:
                    nums.append(num)
                i = j
            else:
                i += 1
        if not nums:
            return None, None
        print(min(nums), max(nums))
        return min(nums), max(nums)

s = Solution()
s.FindMinMaxNumber('12hjk134k431uihjk123', 10, 10000)
