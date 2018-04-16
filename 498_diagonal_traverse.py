class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 这道题不难，主要是分析清楚几种情况，分别该做什么处理
        if not matrix or len(matrix) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])
        output = [0 for _ in range(m * n)]
        row = col = 0
        d = 1

        for i in range(m * n):
            output[i] = matrix[row][col]

            row -= d
            col += d

            if row >= m:
                row = m - 1
                col += 2
                d = -d
            if col >= n:
                col = n - 1
                row += 2
                d = -d
            if row < 0:
                row = 0
                d = -d
            if col < 0:
                col = 0
                d = -d

        return output

