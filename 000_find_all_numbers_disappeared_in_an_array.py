class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        一开始的想法比较幼稚, 其实想的还是排序
        这个解答用的是正负标记法, 如果 x 出现了, 就把 nums[x-1] 设为负数
        因为只要使用 abs, 就相当于没有损失信息, 而且还额外标记了信息
        :type nums: List[int]
        :rtype: List[int]
        """
        for x in nums:
            nums[abs(x) - 1] = -abs(nums[abs(x) - 1])

        return [i + 1 for i, x in enumerate(nums) if x > 0]


if __name__ == '__main__':
    test = [4, 3, 2, 7, 8, 2, 3, 1, 1]
    print(Solution().findDisappearedNumbers(test))
