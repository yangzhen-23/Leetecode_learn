"""
438. 找到字符串中所有字母异位词
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
"""
from typing import List, Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        windows = Counter()
        ans = []
        l = 0

        for r in range(len(s)):
            windows[s[r]] += 1

            if r - l + 1 > len(p):
                windows[s[l]] -= 1

                if windows[s[l]] == 0:
                    del windows[s[l]]
                l += 1

            if r - l + 1 == len(p) and need == windows:
                ans.append(l)
        return ans

        
s = Solution()
string = "abab"
p = "ab"
ans = s.findAnagrams(string, p)
print(ans)
