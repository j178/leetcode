# Author: John Jiang
# Date  : 2016/7/28
import unittest


def two_sum(numbers, target):
    map = {}
    for i, v in enumerate(numbers):
        index = map.get(target - v)
        if index:
            return index + 1, i + 1
        else:
            map[v] = i


def two_sum_1(sorted_nums, target):
    """使用两个指针分别从两头开始查找"""
    i = 0
    j = len(sorted_nums) - 1
    while i < j:
        sum = sorted_nums[i] + sorted_nums[j]
        if sum > target:
            j -= 1
        elif sum < target:
            i += 1
        else:
            return i + 1, j + 1

    raise Exception('No two sum solution')


def two_sum_2(sorted_nums, target):
    def bsearch(key, start):
        low = start
        high = len(sorted_nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if key < sorted_nums[mid]:
                high = mid - 1
            elif key > sorted_nums[mid]:
                low = mid + 1
            else:
                return mid
        return -1

    for i, v in enumerate(sorted_nums):
        j = bsearch(target - v, i)
        if j != -1:
            return i + 1, j + 1

    raise Exception('No two sum solution')


class Test(unittest.TestCase):
    def setUp(self):
        self.nums = [i for i in range(100)]

    def test_two_sum(self):
        res = two_sum(self.nums, 43)
        res1 = two_sum_1(self.nums, 43)
        res2 = two_sum_2(self.nums, 43)
        self.assertEqual(res1, res2)
        print(res)

if __name__ == '__main__':
    unittest.main()
