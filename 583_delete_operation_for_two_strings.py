class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 最开始的想法就是，求两个字符串的最大子序列，然后最少的删除步数就是 len(word1) + len(word2) - 2 * lcs
        # 对于最长公共子串问题，有后缀数组和动态规划两种常用的算法

        # 但是其实…我误解了这道题
        # 因为删除可以删除任意一个元素，比如 park 和 spake, 两者最终相同的部分应该是 pak 而不是 pa
        # 所以这是一个求最长子序列的问题！
        # 所幸，最长子序列和最长子串的状态转移方程只有一点不一样而已

        return len(word1) + len(word2) - 2 * self.lcs(word1, word2)

    def lcs(self, s1, s2):
        len1, len2 = len(s1), len(s2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for x in range(len1 + 1):
            for y in range(len2 + 1):
                if x == 0 or y == 0:
                    dp[x][y] = 0
                elif s1[x - 1] == s2[y - 1]:
                    dp[x][y] = dp[x - 1][y - 1] + 1
                else:
                    dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])

        return dp[len1][len2]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance('park', 'spake'))
