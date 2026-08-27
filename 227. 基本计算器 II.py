"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。
你可以假设给定的表达式总是有效的。所有中间结果将在 [-231, 231 - 1] 的范围内。
注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

示例 1：

输入：s = "3+2*2"
输出：7
示例 2：

输入：s = " 3/2 "
输出：1
示例 3：

输入：s = " 3+5 / 2 "
输出：5
"""

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        n = len(s)
        stack = []
        preSign = '+'
        num = 0

        for i in range(n):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
            if s[i] in '+-*/' or i == n - 1:
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                elif preSign == '/':
                    stack.append(int(stack.pop() / num))
                preSign = char
                num = 0
        print(sum(stack))
        return sum(stack)



s = Solution()
s.calculate("3+1* 12")