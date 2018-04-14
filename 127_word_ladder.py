# 无权图最短路径问题：广度优先搜索

from collections import deque


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        self.alpha = frozenset('abcdefghijklmnopqrstuvwxyz')
        self.word_list = set(wordList)
        seperater = object()  # 用于分隔各层，方便计算 path 长度，即搜索的层数
        step = 1
        queue = deque()
        queue.append(beginWord)
        queue.append(seperater)
        # 入队后就从字典中删除，避免其他词又找回来，不过也可以用一个 visited 的 集合记录已经访问过的节点
        self.word_list.discard(beginWord)
        while queue:
            cur = queue.popleft()
            if cur is seperater:
                step += 1
                continue
            elif cur == endWord:
                return step

            for next_word in self.find_next_words(cur):
                queue.append(next_word)
            # 何时增加步数也很容易出错
            # 可以用计数的方式，当遍历完一层的所有节点后，step +1
            # 这里使用一个特殊的标记，当一层的所有节点都完成后，队列的队首就会是特殊的标记
            # 这时就再向队列中加一个标记，表示新的层开始
            if queue[0] is seperater:
                queue.append(seperater)

        return 0

    def find_next_words(self, word):
        for i, c in enumerate(word):
            for other in self.alpha - set(c):
                new_word = word[:i] + other + word[i + 1:]
                if new_word in self.word_list:
                    yield new_word
                    self.word_list.discard(new_word)


if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength("hit",
                         "cog",
                         ["hot", "dot", "dog", "lot", "log", "cog"]))
