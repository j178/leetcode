class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        d = [None for _ in range(len(nums))]

        d[0] = nums[0]
        d[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            d[i] = max(d[i - 2] + nums[i], d[i - 1])

        return d[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 1, 1]))
