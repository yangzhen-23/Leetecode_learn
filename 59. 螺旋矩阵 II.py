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


# 2026年7月16日 23点37分 我又回来了！！！
# 2026年7月19日 10点53分 水一下时间
# 2026年7月20日 18点53分 再水一下，今天去办理万事达卡了
