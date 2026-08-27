"""
题4：判断质数
给定一个正整数，判断其是否包含相同数字且是否为质数，如果不包含相同数字且为质数，返回true,否则返回false
"""

class Solution:
    def isSpecialPrime(self, n: int) -> bool:
        s = str(n)
        if len(s) != len(set(s)):
            return False

        if n < 2:
            return False

        i = 2
        while i*i < n:
            if n % i == 0:
                return False
            else:
                i += 1
        return True