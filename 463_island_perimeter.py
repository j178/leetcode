class Solution(object):
    def surrounded_cells(self, x, y):
        grid = self.grid
        n = 0
        if x > 0:
            n += grid[x - 1][y]
        if x < len(grid) - 1:
            n += grid[x + 1][y]
        if 0 < y:
            n += grid[x][y - 1]
        if y < len(grid[0]) - 1:
            n += grid[x][y + 1]
        return n

    # naive solution
    # 遍历每个方块，如果是 1，计算它周围的方块数
    # 它周围每多一个方块，island 的总周长就会减一
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        self.grid = grid
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell:
                    n = self.surrounded_cells(x, y)
                    perimeter += (4 - n)

        return perimeter

    def islandPerimeter2(self, grid):
        # 从上到下遍历每个方块，计算总的 island 数 和 neighbor 数目
        # perimeter = island * 4 - neighbor * 2
        # 因为每个 neighbor 会使两条边消失
        islands = 0
        neighbors = 0
        for x, _ in enumerate(grid):
            for y, _ in enumerate(grid[x]):
                if grid[x][y] == 1:
                    islands += 1
                    # 计算右边的邻居
                    if x < len(grid) - 1 and grid[x + 1][y]:
                        neighbors += 1
                    # 计算下边的邻居
                    if y < len(grid[0]) - 1 and grid[x][y + 1]:
                        neighbors += 1

        return islands * 4 - neighbors * 2


if __name__ == '__main__':
    s = Solution()
    print(s.islandPerimeter2([[0, 1, 0, 0],
                              [1, 1, 1, 0],
                              [0, 1, 0, 0],
                              [1, 1, 0, 0]]))
