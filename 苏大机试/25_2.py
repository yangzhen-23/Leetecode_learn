"""
给定一个正整数数组arr,一个目标数字num,若数组中的正整数的“中位数”如果等于目标数字，则返回该整数，如果有多个匹配的结果，返回最大的数。
若正整数的位数是奇数，“中位数”就是中间的数字（如：123 -> 2）
若正整数的位数是偶数，“中位数”就是中间偏左的数字（如：1234 -> 2）
"""
from typing import List
class Solution:
    def FindMaxNumber(self, arr: List[int], num: int) -> int:
        ans = -1

        for x in arr:
            s = str(x)
            mid_index = (len(s) - 1) // 2
            middle = int(s[mid_index])
            if middle == num:
                ans = max(ans, x)
        return ans

sol = Solution()
print(sol.FindMaxNumber([183,22822,76897,8888],8))