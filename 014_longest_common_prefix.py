class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        while True:
            equal = True
            for j in range(len(strs) - 1):
                if len(strs[j]) <= i or len(strs[j + 1]) <= i:
                    equal = False
                    break
                if strs[j][i] != strs[j + 1][i]:
                    equal = False
                    break
            if not equal:
                break
            i += 1
        return strs[0][:i]

    def longestCommonPrefix2(self, strs):
        if len(strs)==0:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if prefix == '':
                    return ''
        return prefix


if __name__ == '__main__':
    strs = ['123', '123', '12345']
    s = Solution().longestCommonPrefix2(strs)
    print(s)
