# https://leetcode.com/problems/majority-element-ii/
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# ----------------------------------------------------------------------------------------------------------------------
def maj_elem(A):

    dct = {}
    for a in A:
        if a in dct:
            dct[a]+=1
        else:
            dct[a]=1

    res = []
    for k,v in dct.items():
        if v>len(A)/3:
            res.append(k)

    return res
# ----------------------------------------------------------------------------------------------------------------------
def maj_elem2(A):

    count1, count2, candidate1, candidate2 = 0, 0, None, None
    for a in A:
        if   a == candidate1:count1 += 1
        elif a == candidate2:count2 += 1
        elif count1 == 0:candidate1, count1 = a, 1
        elif count2 == 0:candidate2, count2 = a, 1
        else:count1, count2 = count1 - 1, count2 - 1

    #res = [n for n in (candidate1, candidate2) if A.count(n) > len(A)//3]
    res = []
    if A.count(candidate1)>len(A)/3:
        res.append(candidate1)

    if A.count(candidate2)>len(A)/3:
        res.append(candidate2)

    return res
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    A = [3,2,3]
    A = [2, 2, 1, 3]

    res = maj_elem2(A)
    print(res)