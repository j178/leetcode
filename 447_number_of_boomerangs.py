class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 这道题其实就是要求各个点之间的距离，然后将距离一个点相同的其他点聚在一个组里，然后就是一个简单的排列组合的问题
        # 如果有两个点b,c 到 a 点距离相等，因为题目说 the order of the tuple matters，所以 abc 和 acb 都是合法的回旋镖
        # 如果有三个点 bcd 到 a 点距离相等，那么从 bcd 三个点中任取两个点做排列，所以结果是 A(3,2) 结果是 6

        cnt = 0
        if not points:
            return cnt
        for i in range(len(points)):
            map = {}
            for j in range(len(points)):
                a = points[i][0] - points[j][0]
                b = points[i][1] - points[j][1]
                d = a * a + b * b
                map[d] = map.get(d, 0) + 1
            # A(n,2) == n*(n-1)
            cnt += sum(n * (n - 1) for n in map.values())

        return cnt
