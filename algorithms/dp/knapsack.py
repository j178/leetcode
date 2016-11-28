def knapsack(w, v, c):
    """

    :param list w: w[i] weight of i-th item
    :param list v: v[i] value of i-th item
    :param int c: capacity of the knapsack
    :return: list m
    """
    n = len(w)
    m = [[0] * (c + 1) for x in range(n + 1)]

    # 初始化m[n]行
    jmax = min(w[n - 1] - 1, c)
    for j in range(jmax + 1):
        m[n][j] = 0
    for j in range(w[n - 1], c + 1):
        m[n][j] = v[n - 1]

    for i in range(n - 1, 1, -1):
        jmax = min(w[i - 1] - 1, c)
        for j in range(jmax + 1):
            m[i][j] = m[i + 1][j]
        for j in range(w[i - 1], c + 1):
            m[i][j] = max(m[i + 1][j], m[i + 1][j - w[i - 1]] + v[i - 1])

    m[1][c] = m[2][c]
    if c >= w[0]:
        m[1][c] = max(m[1][c], m[2][c - w[0]] + v[0])

    return m


if __name__ == '__main__':
    w = [2, 1, 3, 2]
    v = [12, 10, 20, 15]
    c = 5
    m = knapsack(w, v, c)
    print('\n'.join(str(x) for x in m))
