# Author: John Jiang
# Date  : 2016/7/28

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if *my number* is lower, 1 if my number is higher, otherwise return 0

# 简单的二分查找, 但是还是很可能出错, 主要在于初始的数组范围,判断条件以及边界的缩小要一致, 我到现在还是不理解
# 另外一个是要理解题意, 题目说的是my number如果小, guess()返回-1, 不要弄错了.

guess = lambda x: 4 - x


class Solution(object):
    def guess_number(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        # 因为右边界n要取, 所以下面的判断条件要带上=号, 后面的边界更新也要-1, 不然因为判断条件的=号会造成死循环
        # 记住几点: 1. 判断条件带=号, 后面就必须-1, 不然会死循环
        #          2. 如果边界右边可取, 则判断条件就必须带=号, 不然会漏掉
        while low <= high:
            mid = (low + high) // 2
            r = guess(mid)
            if r < 0:
                high = mid - 1
            elif r > 0:
                low = mid + 1
            else:
                return mid
        return -1


print(Solution().guess_number(10))
