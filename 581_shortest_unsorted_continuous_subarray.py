# Created by j178 at 2018/04/22 21:28

"""
581 Shortest Unsorted Continuous Subarray

Given an integer array, you need to find one **continuous subarray** that if
you only sort this subarray in ascending order, then the whole array will be
sorted in ascending order, too.

You need to find the **shortest** such subarray and output its length.

**Example 1:**  

    
    
    **Input:** [2, 6, 4, 8, 10, 9, 15]
    **Output:** 5
    **Explanation:** You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
    

**Note:**  

  1. Then length of the input array is in range [1, 10,000].
  2. The input array may contain duplicates, so ascending order here means **< =**. 




AC Rate: 29.4%

Sample Test Case:
  [2,6,4,8,10,9,15]

"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思想是：从左往右遍历，记录沿途中的最大值，如果遍历过程中有值比 max 小，说明这个数字不符合升序的要求，
        # 就暂时将这个点即为子数组的终点 end
        # 同样的，从右往左遍历，记录途中的最小值 min, 如果有比 min 大的值，记录为子数组的起点 start
        # 如果最终 start > end, 表示整个数组都是有序的
        if not nums or len(nums) == 1:
            return 0
        start = -1
        end = -2
        ma = nums[0]
        mi = nums[-1]
        n = len(nums)
        for i in range(1, n):
            ma = max(nums[i], ma)
            mi = min(nums[n - i - 1], mi)
            if nums[i] < ma:
                end = i
            if nums[n - i - 1] > mi:
                start = n - i - 1

        return end - start + 1


if __name__ == '__main__':
    s = Solution()
    print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
