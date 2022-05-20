# https://leetcode.com/problems/sliding-window-maximum/
# ----------------------------------------------------------------------------------------------------------------------
from collections import deque
# ----------------------------------------------------------------------------------------------------------------------
def maxSlidingWindow(A, k):

    deq = deque()
    result = []

    for i in range(k):
        while len(deq) != 0:
            if A[i] > A[deq[-1]]:
                deq.pop()
            else:
                break

        deq.append(i)

    # Here we will have deque with index of maximum element for the first subsequence of length k.

    # Now we will traverse from k to the end of array and do 4 things
    # 1. Appending left most indexed value to the result
    # 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
    # 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
    # 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)

    for i in range(k, len(A)):
        result.append(A[deq[0]])

        if deq[0] < i - k + 1:
            deq.popleft()

        while len(deq) != 0:
            if A[i] > A[deq[-1]]:
                deq.pop()
            else:
                break

        deq.append(i)

    result.append(A[deq[0]])

    return result

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    A = [1,3,-1,-3,5,3,6,7]
    k = 3

    res = maxSlidingWindow(A,k)
    print(res)