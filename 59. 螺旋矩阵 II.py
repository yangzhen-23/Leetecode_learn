"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，
且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
"""
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        count = 1
        start_index = 0
        while not count >= n ** 2:
            for j in range(start_index, n - 1 - start_index):
                mat[start_index][j] = count
                count += 1
            for i in range(start_index, n - 1 - start_index):
                mat[i][n - 1 - start_index] = count
                count += 1
            for j in range(n - 1 - start_index, start_index, -1):
                mat[n - 1 - start_index][j] = count
                count += 1
            for i in range(n - 1 - start_index, start_index, -1):
                mat[i][start_index] = count
                count += 1
            start_index += 1

        if n % 2 == 1:
            mat[n // 2][n // 2] = count
        return mat

if __name__ == '__main__':
    n = 3
    sol = Solution()
    print(sol.generateMatrix(n))

"""
# 思路
    1. 创建一个 n x n 的矩阵 mat，并初始化为 0。
    2. 使用一个计数器 count 来跟踪当前要填充的数字，从  1 开始。
    3. 使用一个 start_index 来表示当前螺旋的起始位置。
    4. 使用一个 while 循环，直到 count 大于等于 n^2。
    5. 在每一层螺旋中，按顺时针方向填充矩阵。
        - 先填充顶部行，从 start_index 开始，到 n - 1 - start_index。
        - 然后填充右侧列，从 start_index 开始，到 n - 1 - start_index。
        - 最后填充底部行，从 n - 1 - start_index 开始，到 start_index。
        - 最后填充左侧列，从 n - 1 - start_index 开始，到 start_index。
        - 增加 start_index，准备填充下一层螺旋。
    6. 如果 n 是奇数，则在矩阵的中心位置填充最后一个数字。
        - 计算中心位置的索引，即 n // 2。
        - 将最后一个数字 count 赋值给 mat[n // 2][n。 
        - 返回 mat。
"""
