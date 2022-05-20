# https://leetcode.com/problems/top-k-frequent-elements
import heapq
from collections import Counter
# ----------------------------------------------------------------------------------------------------------------------
def top_frequent(A,k):
    res = []
    dic = Counter(A)

    my_heap = [(-val, key) for key, val in dic.items()]
    heapq.heapify(my_heap)

    print(my_heap)

    for i in range(k):
        value = heapq.heappop(my_heap)[1]
        res.append(value)
    return res
# ----------------------------------------------------------------------------------------------------------------------
def top_frequent2(A,k):

    cnt = Counter(A)
    C = [2,3,4,5,6,2,3]

    myheap = [c for c in C]
    print(myheap)


    heapq.heapify(myheap)
    print(myheap)
    #
    # res = [myheap.pop()[1] for kk in range(k)]

    return res
# ----------------------------------------------------------------------------------------------------------------------
def find_interval(A, d):
    left, right = 0, 1
    min_value = max_value = A[0]
    res = 1
    while (right < len(A)):
        # attemp shift right
        max_value = max(max_value, A[right])
        min_value = min(min_value, A[right])
        if (max_value - min_value <= d):
            res = (max(res, right - left) >= res)
            right += 1

        else:  # attempt shift left
            left += 1

    return res
# ----------------------------------------------------------------------------------------------------------------------
def find_interval2(A, d):
    left, right = 0, 1
    min_value = max_value = A[0]
    res = right-left

    while (right+1<len(A)):
        right += 1
        #attempt shift right
        max_value = max(max_value, A[right])
        min_value = min(min_value, A[right])
        if (max_value - min_value <= d):
            res =max(res, right - left)
        else:
            left+=1

    return res
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    A = [1,1,1,2,2,5,5,5,5,5,3]
    d = 2

    res = find_interval2(A,d)
    print(res)


