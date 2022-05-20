# Combination Sum III
# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# ----------------------------------------------------------------------------------------------------------------------
def cmb(k,S,D=[1, 2, 3, 4, 5, 6, 7, 8, 9]):

    if k==1:
        if S in D:return [[S]]
        return []

    res = []
    for i,d in enumerate(D):
        new_d = [dd for dd in D if dd>d]
        res_temp = cmb(k-1,S-d,new_d)
        for r in res_temp:
            res.append([d]+r)

    return res
# ----------------------------------------------------------------------------------------------------------------------
def cmb2(k,S):

    D = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    queue = []
    res = []
    for d in D:
        queue.append([d])

    while len(queue)>0:
        seq_d = queue.pop()
        if sum(seq_d)==S and len(seq_d)==k:
            res.append(seq_d)
        elif sum(seq_d)>S:
            continue
        else:
            for d in range(1+max(seq_d),10):
                queue.append(seq_d+[d])

    return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    k = 3
    S = 9

    res = cmb2(k,S)
    print(res)