class Solution(object):
    def findDuplicates(self, nums, a, b, c):
        ans = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                ans.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return ans


if __name__ == '__main__':
    t = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDuplicates(t))
