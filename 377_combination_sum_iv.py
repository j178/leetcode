# Author: John Jiang
# Date  : 2016/7/30

# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that
# add up to a positive integer target.

# Example:
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?


def combinationSum4(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # 举例 nums=[1,2,3] targe=4
    dp = [0] * (target + 1)
    dp[0] = 1
    for x in range(target + 1):
        for y in nums:
            if x + y <= target:
                dp[x + y] += dp[x]
    return dp[target]
