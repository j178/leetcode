# Created by j178 at 2018/04/23 22:46

"""
390 Elimination Game

There is a list of sorted integers from 1 to _n_. Starting from left to right,
remove the first number and every other number afterward until you reach the
end of the list.

Repeat the previous step again, but this time from right to left, remove the
right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to
left, until a single number remains.

Find the last number that remains starting with a list of length _n_.

**Example:**

    Input:
    n = 9,
    _1_ 2 _3_ 4 _5_ 6 _7_ 8 _9_
    2 _4_ 6 _8_
    _2_ 6
    6
    
    Output:
    6
    

AC Rate: 42.6%

Sample Test Case:
  9

"""


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 这题主要是注意到 left_to_right/right_to_left 之后，last_remaning 的关系
        return self.left_to_right(n)

    def left_to_right(self, n):
        if n == 1:
            return 1
        # 一次从左到右的操作，不管 n 的长度是奇数还是偶数，结果都是一样
        # L(1,2,3,4) = R(2,4) = 2 * R(1,2)
        return 2 * self.right_to_left(n // 2)

    def right_to_left(self, n):
        if n == 1:
            return 1

        # R(1,2,3,4,5) = L(2,4) = 2 * L(1,2)
        if n % 2 == 1:
            return 2 * self.left_to_right(n // 2)
        # R(1,2,3,4) = L(1,3) = 2 * L(1,2) - 1
        # 恰好存在这样的关系
        # 就是为了想方设法将 L(n) 的问题，转为 R(n//2)
        else:
            return 2 * self.left_to_right(n // 2) - 1


if __name__ == '__main__':
    s = Solution()
    print(s.lastRemaining(9))
