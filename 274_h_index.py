# Created by John Jiang at 2018/4/17 22:33

class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        citations = sorted(citations, reverse=True)
        n = len(citations)
        i = 0
        while i < n and citations[i] >= i + 1:
            i += 1
        return i

    def h_index2(self, citations):
        # 使用数组作为 hash 表，加快速度
        if not citations:
            return 0
        n = len(citations)
        # count[i] 表示引用次数为 i 的文章数量
        count = [0] * (n + 1)
        for i in citations:
            # 对于引用次数超过 n 的文章，记在 n 头上
            count[min(n, i)] += 1

        for i in range(len(count), -1, -1):
            if count[i] >= i:
                return i
            count[i - 1] += count[i]


if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([3, 0, 6, 1, 5]))
