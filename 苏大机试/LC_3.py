"""
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
"""
# 暴力
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j + 1]
                if len(sub) == len(set(sub)):
                    ans = max(ans, len(sub))
        return ans

# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n =len(s)
        windows = set()
        l = 0
        ans = 0

        for r in range(n):
            while s[r] in windows:
                windows.remove(s[l])
                l += 1
            windows.add(s[r])
            
            ans = max(ans, r - l + 1)
        return ans