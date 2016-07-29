# Author: John Jiang
# Date  : 2016/7/28


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


def two_sum_2(sorted_nums,target):
    pass
