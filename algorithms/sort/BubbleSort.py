import random


def bubble_sort(num):
    """
    冒泡排序的重点在于内层循环, 遍历的范围要从大到小, 第一次大循环是要选出整个数组中最大/小的元素(由比较的符号确定)
    内层循环的下标从大的开始, 则最先有序的是数组的左侧; 下标从小的开始, 则从左往右冒泡, 右边的元素最先开始有序;
    外层循环的值不重要, 只要知道循环几次就就可以了, 内层循环根据外层的值相应地调整.
    """
    for i in range(len(num)):
        for j in range(len(num) - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]


def bubble_sort_1(num):
    for i in range(len(num)):
        for j in range(len(num) - i - 1, 0, -1):
            if num[j - 1] > num[j]:
                num[j - 1], num[j] = num[j], num[j - 1]


def bubble_sort_2(num):
    global exchange_times
    for i in range(len(num) - 1, 0, -1):
        for j in range(i):
            exchange_times += 1
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]


# 如果在一次大循环中发现没有交换任何值, 因为之后的循环范围会更小, 所以更不会交换值了, 所以整个数组其实已经有序了, 就可以退出循环了
def bubble_sort_3(nums):
    swaped = True

    for i in range(len(nums)):
        if not swaped: break
        swaped = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                swaped = True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


if __name__ == '__main__':
    nums = [random.randint(-50, 100) for x in range(30)]
    print('before', nums)
    bubble_sort_3(nums)
    print('after', nums)
