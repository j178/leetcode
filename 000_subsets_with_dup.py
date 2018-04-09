def get_all_subsets(set):
    if len(set) == 0:
        return [[]]
    if len(set) == 1:
        return [[], set]
    last = set[-1]
    ori_sets = get_all_subsets(set[:-1])
    new_sets = []
    for subset in ori_sets:
        new_subset = subset[:]
        new_subset.append(last)
        new_sets.append(new_subset)
    return ori_sets + new_sets


def get_all_unique_subsets(set):
    if len(set) == 0:
        return [[]]
    if len(set) == 1:
        return [[], set]
    pre_set, last = set[:-1], set[-1]
    dup = pre_set.count(last)
    ori_sets = get_all_unique_subsets(pre_set)
    new_sets = []
    for subset in ori_sets:
        new_subset = subset[:]
        if (not dup) or (last in new_subset and new_subset.count(last)+1>dup):
            new_subset.append(last)
            new_sets.append(new_subset)
    return ori_sets + new_sets

def get_all_unique_subsets2(S:[]):
    # 这个解法真的是碉堡了！
    S.sort()
    res=[[]]
    for i in range(len(S)):
        if i==0 or S[i]!=S[i-1]:
            # l 表示出现重复之前的 res 的长度
            l=len(res)
        for j in range(len(res)-l,len(res)):
            res.append(res[j]+[S[i]])
    return res

print(get_all_unique_subsets2([1,2, 2, 2]))
