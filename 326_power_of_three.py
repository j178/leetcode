# Author: John Jiang
# Date  : 2016/7/28

# Given an integer, write a function to determine if it is a power of three.

# Follow up:
# Could you do it without using any loop / recursion?

# 这种题目最简单的想法应该就是转换成3进制, 如果是3的乘方, 3进制表示应该是1000...


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        # 往右移位
        while n % 3 == 0:
            n //= 3

        return n == 1


print(Solution().isPowerOfThree(3 ** 33 * 3))
