def matrix_chain(p):
    m = [[0] * len(p) for _ in range(len(p))]
    s = [[0] * len(p) for _ in range(len(p))]
    # 单个矩阵的计算量
    for i in range(len(p)):
        m[i][i] = 0

    # r 每次循环矩阵链的长度
    for r in range(2, len(p) + 1):
        # i 为每次开始位置
        for i in range(1, len(p) - r + 1):
            j = i + r - 1

            # 取第一个可断开位置，即从i处断开，前面部分只有一个矩阵
            m[i][j] = m[i + 1][j] + p[i - 1] * p[i] * p[j]
            s[i][j] = i

            for k in range(i + 1, j):
                t = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if t < m[i][j]:
                    m[i][j] = t
                    s[i][j] = k
    return m, s


def traceback(i, j, s):
    if i == j: return
    traceback(i, s[i][j], s)
    traceback(s[i][j] + 1, j, s)

    print('Multiply A', i, ',', s[i][j], ' and A', s[i][j] + 1, ',', j, sep='')


if __name__ == '__main__':
    p = [20, 25, 10, 5, 15, 20]

    m, s = matrix_chain(p)
    # print(m)
    # print(s)
    traceback(1, len(p) - 1, s)
